---
prev: ../getting-started/
---

# Useful Examples

This page provides examples and further context for endpoints that are more difficult to navigate.

All the examples bellow expect that authentication token has already been obtained. Please see [Authentication](../authentication/README.md) for detailed explanation of how to obtain it.

## Device Monitoring

The following examples are relevant for obtaining information about devices in your company.

### Example 1
**Goal**: Get the names and descriptions of devices that are currently offline.  
**Endpoint Section**: *DeviceMonitoring*  
**Endpoint**: `/monitoring/devices/companies/<CompanyId>`  
**Request**:

```bash 
curl -X 'POST' \
  'https://gateway.wadmp3.com/api/monitoring/devices/companies/<INSERT_COMPANY_ID>' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <INSERT_YOUR_ACCESS_TOKEN_HERE>' \
  -H 'Content-Type: application/json-patch+json' \
  -d '{
  "page": 1,
  "page_size": 10,
  "filters": [
    {
      "rule": {
        "operator_id": "Equals",
        "operands": [
          0
        ]
      },
      "field_name": "Online"
    }
  ],
  "fields": [
    {
      "name": "Name"
    },
    {
      "name": "Description"
    }   
  ]
}' 
``` 

**Comments**:  
- A list of all valid values for `field_name` property can be obtained via a `GET /fields` endpoint.  
- Some fields have a property `has_options=true`. For such fields there is a predefined list of possible values that can be set. `Online` field is one of those. If you want to learn what values are possible for such field, you can call `GET /fields/input-options` endpoint. For this particular field it would return:  

```bash
...
[
      {
        "id": 0,
        "name": "Offline"
      },
      {
        "id": 1,
        "name": "Online"
      },
      {
        "id": -1,
        "name": "Never Connected"
      }
],
...
```  

- To obtain a list of possible values for `operator_id` property, you can use endpoint `GET /fields/operators-for-types`.  

### Example 2  
**Goal**: Get the highest CPU usage & the MAC of the router with the highest CPU usage among routers whose tag Country has value “Germany”.  
**Endpoint Section**: *CompanyStatistics*  
**Endpoint**: `/monitoring/companies/<CompanyId>/sources`  
**Request**:  

```bash
curl -X 'POST' \
  'https://gateway.dev.wadmp.com/api/monitoring/companies/<INSERT_COMPANY_ID>/sources' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <INSERT_YOUR_ACCESS_TOKEN_HERE>
  -H 'Content-Type: application/json-patch+json' \
  -d '{
  "filters": [
    {
      "rule": {
        "operator_id": "Equals",
        "operands": [
          "Germany"
        ]
      },
      "field_name": "Country"
    }
  ],
  "sources": [
    <INSERT_MAX_CPU_SOURCE_ID>, <INSERT_TOP_CPU_DEVICE_SOURCE_ID>
  ]
}'
```  

**Comments**:  
- Before you call this endpoint, you need to find the ID of the appropriate Sources. You can use GET /sources endpoint to get a list of all Sources available to your company. In this case you need to look for Sources with the following properties:  
    - `"source_type": "FieldAggregation", "aggregation_type": "Max", "field_id": <INSERT_CPU_FIELD_ID> `
    - `"source_type": "FieldAggregation", "aggregation_type": "TopDevice", "field_id": <INSERT_CPU_FIELD_ID>`  
- **Sources Explanation**:  
    - Whenever a new field is added to a company, the system automaticly creates new Sources for it. Each such Source represents a different type of information, which can be queried. 
    - Not all sources are associated with fields (e.g. Source named `"Users Count"`).

### Example 3  

**Goal**: Get the connection history of a device. 
**Endpoint Section**: *DeviceMonitoring*
**Endpoint**: `/monitoring/devices/<MAC>/history`
**Request**:  

```bash
curl -X 'POST' \
  'https://gateway.dev.wadmp.com/api/monitoring/devices/<INSERT_MAC_ADDRESS>/history' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <INSERT_YOUR_ACCESS_TOKEN_HERE>
  -H 'Content-Type: application/json-patch+json' \
  -d '{
  "fields": [
    "Online"
  ],
  "start": "2025-03-18T12:21:05.684Z",
  "stop": "2025-06-19T12:21:05.684Z"
}'
```  

**Comments**: 
- You can also use the optional `sampling_period` and `sampling_operator` parameters to reduce the amount of data returned by the endpoint. However, those are not very useful for the connection history, so they are not used in this example.  

## Device Management  

The following examples are relevant for applying changes to your devices.  

### Example 1  

**Goal**: Update the value of tag “IsWarm” to True for all routers whose Temperature > 30 °C.  
**Endpoint Section**: *DeviceManagement*  
**Endpoint**: `/management/devices/long-operations/fields`  
**Request**:  

```bash
curl -X 'POST' \
  'https://gateway.dev.wadmp.com/api/management/devices/long-operations/fields' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <INSERT_YOUR_ACCESS_TOKEN_HERE>
  -H 'Content-Type: application/json-patch+json' \
  -d '{
  "company_id": <INSERT_COMPANY_ID>,
  "field_name": "IsWarm",
  "value": true,
  "filters": [
    {
      "rule": {
        "operator_id": "GreaterThan",
        "operands": [
          30
        ]
      },
      "field_name": "Temperature"
    }
  ]
}'
```  

**Comments**:  
- Update is executed asynchronously. This endpoint returns code 202 (Accepted) and the ID of the operation, whose status can then be queried via `/long-operations/<OperationId>` endpoint.


  

