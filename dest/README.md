Exported Dockerfile & its dependencies are located in the same folder. The structure is as below:
- flow: the folder contains chat with pdf flow files
  - ...
- connections: the folder contains yaml files to create all related connections
  - ...
- runit: the folder contains all the runit scripts
  - ...
- Dockerfile: the dockerfile to build the image
- start.sh: the script used in `CMD` of `Dockerfile` to start the service
- settings.json: a json file to store the settings of the docker image
- README.md: the readme file to describe how to use the dockerfile

