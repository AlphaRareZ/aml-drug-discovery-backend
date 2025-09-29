import datetime
import pika
import json
import base64
import os
import json
print("Check Worker.log File")

with open("config.json") as config_file:
    config = json.load(config_file)

# إعداد الاتصال بـ RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=config["RabbitMQ"]["host"])
)
channel = connection.channel()

# تعريف الـ Queues
request_queue = config["RabbitMQ"]["request_queue"]
response_queue = config["RabbitMQ"]["response_queue"]

channel.queue_declare(queue=request_queue, durable=True)
channel.queue_declare(queue=response_queue, durable=True)

# المكان اللي هيتخزن فيه الملفات
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def log(message):
    with open("worker.log", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")
    # print(message)


def process_request(ch, method, properties, body):
    try:
        # Deserialize JSON
        message = json.loads(body)
        file_name = message.get("FileName")
        file_data = message.get("FileData")
        user_id = message.get("UserId")
        analysis_id = message.get("AnalysisID")

        # Decode Base64 -> Save file
        file_bytes = base64.b64decode(file_data)
        file_path = os.path.join(UPLOAD_DIR, file_name)

        with open(file_path, "wb") as f:
            f.write(file_bytes)

        log(f"[✔] Saved file {file_name} for User {user_id}")

        # Build Response
        response = {
            "StatusCode": 200,
            "Message": f"File {file_name} saved successfully and being processed",
            "AnalysisID": analysis_id,
            "UserId": user_id,
            "CompletionDate":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        # log(str(datetime.datetime.now()))
        # Send Response back to .NET
        channel.basic_publish(
            exchange="",
            routing_key=response_queue,
            body=json.dumps(response),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ),
        )

        log(f"[✔] Response sent for AnalysisID: {analysis_id}")

        # Ack the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        log(f"[❌] Error processing message: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


# Start Consuming
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=request_queue, on_message_callback=process_request)

log("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
