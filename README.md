-----

## ⚙️ Requirements

To run this project, you'll need the following software installed on your machine:

  * **.NET 9.0 SDK** 
  * **Rabbit MQ Client**
  * **SQL Server** (version greater than 2019)
  * **Python**

-----

## 🚀 Getting Started

You can easily run the entire application using the provided batch script. This will restore the necessary .NET dependencies and start all three services concurrently in separate windows.

Open your terminal and execute the following command:

```bash
.\Run.bat
```

This script automates the following steps:

1.  Restores dependencies and runs the `AMLService`.
2.  Restores dependencies and runs the `AuthenticationService`.
3.  Starts the `PythonWorker`.

-----

## 🧹 Cleaning the Project

A script is included to clean the build artifacts from the .NET projects. This is useful for removing temporary files and ensuring a fresh build.

To clean the projects, run:

```bash
.\Clean.bat
```

This will execute the `dotnet clean` command within the `AMLService` and `AuthenticationService` directories.
