# Appointment API

This is an app that can get compatible time slots for interviews by taking in availability of interviewer and applicant.

## Installation

Install docker and docker compose on a linux system.
Then clone the repo using the below link :

```bash
https://github.com/neerajvkn/appointment_api.git
```
After cloning, navigate inside the repo directory from a terminal and run

```
docker-compose up --build
```
This will start the docker container for the application and will bind it to port `8000`
## Usage

### To add available schedule of the interviewer or applicant, below api link can be used
```
http://localhost:8000/post_slot/
```
This api takes 4 body paramters `id` , `id_type`, `slot_begining`,  `slot_end`. This is a POST API.

`id` and `id_type` is char type, with max id length of 10 and `slot_begining`,  `slot_end` are integers. 
id type should be either `applicant` or `interviewer`. slot beginning and end should be between 0 to 24 hours and there should be atleast one hour between beginning and end times. beginning cannot be greater that end time. interviewer and applicant can have similar ids since data for both are stored in different models.

EG for interviewer scheduling:
```
{
    "id" : "222",
    "slot_begining" : 17,
    "id_type" : "interviewer",
    "slot_end" : 24
}
```
EG for applicant scheduling:
```
{
    "id" : "111",
    "slot_begining" : 13,
    "id_type" : "applicant",
    "slot_end" : 15 
}
```
Upon successful scheduling, a return will be given saying if the slot if the slot is updated or created. ( Updated if there was already a schedule, created if its new user )
```
"interviewer time slot updated"
```
```
"applicant time slot entered updated"
```

sample error
```
"Unacceptable time slot parameters"
```


### To get compatible slots of interviewer and applicant, below api can be used. This is a GET API.

```
http://localhost:8000/get_slot/
```
This api takes 2 parameters `appl_id` and `intr_id`, both chars, limit 10.
appl_id is the id of the applicant and intr_id is the id of the interviewer. 

EG:
```
{
    "appl_id" : 111,
    "intr_id" : 222
}
```
Upon successful fetching, a JSON response will be provided as a list of lists with all available possible timing. if there is no available slot, that message is relayed.

Sample Response if slots are available

```
[
    [13,14],
    [14,15]
]
```

Error if no slots are available :
```
"No time slots available"
```