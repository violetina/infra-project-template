# Workflow for {{ cookiecutter.project_name }}

This document outlines the standard operating procedure for this infrastructure project.

{% if cookiecutter.workflow_type == 'blue-green' %}
### Blue/Green Deployment Flow

```mermaid
flowchart TD
    A(["1. Setup Requirements"]) --> B["2. Provision New Cluster"]
    B --> C{"3. Test New Cluster"}
    C -- Pass --> D["4. Migrate/Sync Data"]
    C -- Fail --> X(["Halt & Rollback"])
    D --> E{"5. Test Data Sync"}
    E -- Pass --> F["6. Switch Traffic Blue -> Green"]
    E -- Fail --> X
    F --> G(["7. Decommission Old Cluster"])
```

### Execution Steps
- [ ] Verify prerequisites and access.
- [ ] Provision the new isolated environment.
- [ ] Run automated tests against the new environment.
- [ ] Initiate the data replication/sync mechanism.
- [ ] Validate data integrity on the new cluster.
- [ ] Flip the DNS/Load Balancer to route traffic to the new cluster.
- [ ] Wait for TTL/Drain period, then destroy the old cluster.

{% elif cookiecutter.workflow_type == 'in-place-upgrade' %}
### In-Place Upgrade Flow

```mermaid
flowchart LR
    A(["1. Snapshot/Backup"]) --> B["2. Drain Node"]
    B --> C["3. Apply Patch/Upgrade"]
    C --> D{"4. Health Check"}
    D -- Pass --> E["5. Uncordon/Restore Traffic"]
    D -- Fail --> X(["Restore from Backup"])
```

### Execution Steps
- [ ] Take a full disk snapshot or database backup.
- [ ] Drain connections from the target node.
- [ ] Execute the upgrade package.
- [ ] Verify application health locally.
- [ ] Add the node back into the load balancer rotation.

{% else %}
### Standard Project Flow

```mermaid
flowchart LR
    A["Create issue"] --> B["Implement"]
    B --> C["Document"]
    C --> D["Generate docs"]
    D --> E["Review"]
    E --> F["Publish"]
```

### Execution Steps
- [ ] Open a tracking ticket.
- [ ] Write the infrastructure code.
- [ ] Update these documentation files.
- [ ] Submit a Pull Request for review.
{% endif %}

