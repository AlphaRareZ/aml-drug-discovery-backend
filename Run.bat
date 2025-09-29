cd AMLService 

dotnet restore
start dotnet run
cd..

cd AuthenticationService

dotnet restore
start dotnet run
cd..

cd PythonWorker

start python rabbitmq_utils.py

echo .

