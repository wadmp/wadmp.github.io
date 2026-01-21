---
prev: ../csv-import-guide/
next: ../../device-monitoring/
---

## Commands

A **Command** is a request sent from the server to a router, instructing it to perform a specific operation. If a router is offline when a command is created, the server queues it and ensures delivery once the router reconnects.

---

### Command Life Cycle & States

Each command moves through several states during its lifecycle:
- **Created**: The command has been created but not yet sent to the device.
- **AwaitingResponse**: The command has been sent and the server is waiting for a response. 
- **Superseded**: The command was replaced by a newer command of the same type.
- **Failed**: The router responded but was unable to complete the requested operation. A failure reason is provided.
- **Aborted**: The command was manually aborted before completion.
- **Success**: The router successfully executed the request.

---

### Retries and Sequencing

To ensure stability in remote environments, the server follows specific logic for delivery:

#### The Retry Mechanism

If a router does not respond within a reasonable timeframe, the server automatically resends the command. To prevent network congestion, the **retry period increases** with every subsequent attempt. Resending stops once a command reaches a "Finished" state (Success, Failed, or Aborted).

#### Sequential Handling

Commands of the **same type** are handled sequentially based on their creation date. For example, if you issue two "Reboot" commands, the system waits for the first reboot to complete or fail before initiating the second one.

#### Superseding Commands

If multiple commands of the same type are in the **Created** state, the server will only process the **newest** one. All older, unsent commands of that type will be marked as **Superseded** to ensure the router only performs the most up-to-date request.

---

### Command Types

Currently, the following command types are supported:

| Command Type        | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Reboot              | Triggers a hardware restart of the remote router.                           |
| Rebootstrap         | Forces the device to re-initialize its connection to the management server. |
| ApplyConfigProfile  | Pushes a new desired state/configuration to the device.                     |
| ReadConfig          | Requests the current running configuration from the router.                 |

---

### Impact on Sync Status
The SyncStatus of a router is specifically tied to `ApplyConfigProfile` commands. Other command types (like Reboot) do not affect this status.

- **Pending**: There is at least one unfinished `ApplyConfigProfile` command in the queue.
- **Synced**: All `ApplyConfigProfile` commands have finished successfully.
- **Failed**: All `ApplyConfigProfile` commands are finished, but the most recent one ended in a **Failed** state.

> **Note**: Because SyncStatus relies on the latest configuration attempt, you cannot **Abort** the newest `ApplyConfigProfile` command. Doing so would result in an inaccurate "Synced" status when the device might not actually match the server's intended configuration.

---

### Managing Commands in the UI

You can monitor and manage commands directly from the **Device Page**:

- **Commands Tab**: Displays a table of all existing commands, including their type, current state, and creation timestamps.
- **Command Details**: Click the **Detail** button next to any command to view granular information, such as the specific reason for a failure or the scheduled time for the next retry.
- **Aborting Commands**: An **Abort** button is available next to eligible commands. This allows you to stop the server from further retry attempts for that specific request.
- **Data Retention**: To keep the interface clean, records of finished commands are automatically removed from the system after a few weeks.
