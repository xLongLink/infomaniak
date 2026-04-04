# eTickets Overview

This section contains the `etickets` resources for the Infomaniak Python SDK.

All methods listed below are currently placeholders and raise `NotImplementedError`.

## Nested Resources

- `address`
- `customers`
- `date`
- `reservations`
- `surveys`
- `ticket`

## SDK Function Coverage

| Resource methods                          | HTTP call                                        | Implemented |
| ----------------------------------------- | ------------------------------------------------ | ----------- |
| `etickets.address.list`                   | `GET /2/etickets/address`                        | No          |
| `etickets.customers.logs`                 | `GET /2/etickets/customers/{customer_id}/logs`   | No          |
| `etickets.date.list`                      | `GET /2/etickets/date`                           | No          |
| `etickets.reservations.display_by_id`     | `GET /2/etickets/reservation/{reservation_id}`   | No          |
| `etickets.reservations.display_by_uuid`   | `GET /2/etickets/reservation/{reservation_uuid}` | No          |
| `etickets.surveys.list`                   | `GET /2/etickets/surveys`                        | No          |
| `etickets.surveys.answers.tickets.list`   | `GET /2/etickets/surveys/answers/tickets`        | No          |
| `etickets.surveys.answers.tickets.update` | `PATCH /2/etickets/surveys/answers/tickets`      | No          |
| `etickets.surveys.answers.passes.list`    | `GET /2/etickets/surveys/answers/passes`         | No          |
| `etickets.surveys.answers.passes.update`  | `PATCH /2/etickets/surveys/answers/passes`       | No          |
| `etickets.ticket.update`                  | _pending OpenAPI confirmation_                   | No          |
