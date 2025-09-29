-----

## ⚙️ Requirements

To run this project, you'll need the following software installed on your machine:

  * [cite\_start]**.NET 9.0 SDK** [cite: 1]
  * [cite\_start]**Rabbit MQ Client** [cite: 1]
  * [cite\_start]**SQL Server** (version greater than 2019) [cite: 1]
  * [cite\_start]**Python** [cite: 1]

-----

## 🚀 Getting Started

You can easily run the entire application using the provided batch script. This will restore the necessary .NET dependencies and start all three services concurrently in separate windows.

Open your terminal and execute the following command:

```bash
.\Run.bat
```

This script automates the following steps:

1.  [cite\_start]Restores dependencies and runs the `AMLService`. [cite: 2]
2.  [cite\_start]Restores dependencies and runs the `AuthenticationService`. [cite: 2]
3.  [cite\_start]Starts the `PythonWorker`. [cite: 2]

-----

## 🧹 Cleaning the Project

A script is included to clean the build artifacts from the .NET projects. This is useful for removing temporary files and ensuring a fresh build.

To clean the projects, run:

```bash
.\Clean.bat
```

[cite\_start]This will execute the `dotnet clean` command within the `AMLService` and `AuthenticationService` directories. [cite: 3]
