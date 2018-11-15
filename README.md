# AirBnB_clone
---

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20181114%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20181114T223110Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f3d410d7052445a3d5c69225e5ce2d169b2c13250bc9dc95f730dca122267f9e)

## Description

This is a repository for the first segment of the AirBnB clone we will be creating for the next four months.
This project will consist of six parts:
* The console
* Web static
* MySQL storage
* Web framework - templating
* RESTful API
* Web Dynamic

This repo contains the first part: the console. The console is the storage system that will hold all the future objects that we will implement in the later parts of the project.

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20181115%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20181115T012613Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f0e5bec5a9989bfc7da9a5c665353d0dd1a049d4a50517624885b9d11ea1df7d)

---
## Files
---
File|Task
---|---
console.py | Main console file
amenity.py | Amenity class
base_model.py | BaseModel class template
city.py | City class
place.py | Place class
review.py | Review class
state.py | State class
user.py | User class
file_storage.py | FileStorage class
test_console.py | Unittest module for console
test_amenity.py | Unittest module for amenity
test_base_model.py | Unittest module for base model
test_city.py | Unittest module for city
test_place.py | Unittest module for place
test_review.py | Unittest module for review
test_state.py | Unittest module for state
test_user.py | Unittest module for user
test_file_storage.py | Unittest module for file storage

Directory Name | Description
---|---
models | Contains all the classes
models/engine | Contains JSON conversion files
tests/test_models | Contains unittest files
tests/test_models/test_engine | Contains unittest file for the engine

## Authors
Damon Nyhan
Leo Byeon
