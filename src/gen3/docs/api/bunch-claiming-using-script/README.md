
## Bunch Claiming Devices Using Script

This topic is a tutorial for bunch claiming devices using API, Python scripts, and CSV files.

### Requirements

1. Python

2. DMP library

- Download latest repository from [https://bitbucket.org/bbsmartworx/dmp-public](https://bitbucket.org/bbsmartworx/dmp-public):

  - [Direct link to download as ZIP file](https://bitbucket.org/bbsmartworx/dmp-public/get/00b7e5bd78a6.zip)

- Extract the ZIP file and go to folder:

```
\bbsmartworx-dmp-public-00b7e5bd78a6\gen3\python_scripts\lib>
```

- Install build dependency: **pip3 install build.**

- Build the dmp library like this:

```
python3 -m build
\bbsmartworx-dmp-public-00b7e5bd78a6\gen3\python_scripts\lib>python3 -m build
```

- You should see build status coming up:
  ![build status](../images/bunch-claiming-devices/build-status.png)

- If build is sucesfull you should see:
  ![build is sucesfull](../images/bunch-claiming-devices/build-is-sucesfull.png)

- Then you can proceed with installing the dmp library by going into the dist folder:
  ![dist folder](../images/bunch-claiming-devices/dist-folder.png)

- And execute pip install **dmp-3.0.3.tar.gz** (in the dist folder)

- If everything goes well you should be able to list the dmp library by pip3 list:
  ![dmp library](../images/bunch-claiming-devices/dmp-library.png)

3. Clone of the DMP repository that contains python_scripts (ZIP file from the previous step should contain this): [https://bitbucket.org/bbsmartworx/dmp-public](https://bitbucket.org/bbsmartworx/dmp-public)

### Execution

- Once you will have downloaded the DMP library and the DMP repository, head to the folder:

```
bbsmartworx-dmp-public-00b7e5bd78a6\gen3\python_scripts\csv_utilities
```

- Edit the example.csv file to include all the devices you want to claim.

![CSV_example](../images/bunch-claiming-devices/CSV_example.png "CSV Example")

- Once example.csv is ready, open the command line and navigate to the repository folder:

```
\python_scripts\csv_utilities\
```

- Execute the following command:

```
python claim_devices.py -username "WADMP_EMAIL" -password "PASSWORD" example.csv "COMPANY_NAME"
```

::: warning Caution:
Please note that the Company name parameter is CASE SENSITIVE!
:::

![ConsoleExample_1](../images/bunch-claiming-devices/ConsoleExample_1.png "Console Example 1")

- Example Command (_from the_ \python*scripts\csv_utilities\ \_folder*):

```
python claim_devices.py -username user@wadmp.com -password S3CR3T_PASS example.csv AdvantechTest
```

![ConsoleExample_2](../images/bunch-claiming-devices/ConsoleExample_2.png "Console Example 2")

- If the script executes successfully, the device will be claimed to your company.

![ConsoleExample_3](../images/bunch-claiming-devices/ConsoleExample_3.png "Console Example 3")

- If there is an issue with claiming the device, an error message will be displayed:

![ConsoleExample_4](../images/bunch-claiming-devices/ConsoleExample_4.png "Console Example 4")
