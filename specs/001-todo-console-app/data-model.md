# Data Model: In-Memory Todo Console Application

This document defines the data entities for the project, as extracted from the feature specification.

## Entities

### Task

Represents a single todo item.

**Attributes**:

| Attribute   | Type    | Description                      | Constraints          |
|-------------|---------|----------------------------------|----------------------|
| `id`        | integer | Unique identifier for the task   | Mandatory, Unique    |
| `title`     | string  | The title of the task            | Mandatory            |
| `description` | string  | An optional description of the task | Optional             |
| `completed` | boolean | The completion status of the task| Mandatory, Default: false |
