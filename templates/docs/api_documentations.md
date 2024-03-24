# Event API

## Overview

The Event API provides endpoints to retrieve and create events.

## Base URL

`/api/events/`

## Endpoints

### Post Events

### Get Events

#### URL

`GET /api/events/`

`POST /api/events/`

#### Description

Creating events

Retrieve upcoming, active, and past events.

#### Response

- `200 OK` on success




# Event Detail API

## Overview

The Event Detail API provides endpoints to retrieve and update specific event details.

## Base URL

`/api/events/<int:pk>/`

## Endpoints

### Get Event Detail

#### URL

`GET /api/events/<int:pk>/`

#### Description

Retrieve details of a specific event.

Update deatails of a specific event.

#### Parameters

- `pk` (integer, required): Primary key of the event.

#### Response

- `200 OK` on success


```json
{
    "upcoming-events": [Array of upcoming event objects],
    "active-events": [Array of active event objects],
    "past-event": [Array of past event objects]
}

{
    "name": "Example Event",
    "start_datetime": "YYYY-MM-DDTHH:MM:SSZ",
    "end_datetime": "YYYY-MM-DDTHH:MM:SSZ"
}

{
    "id": "ID of the created event",
    "name": "Name of the event",
    "start_datetime": "Start datetime of the event",
    "end_datetime": "End datetime of the event"
}

{
    "error": "Description of the error"
}




