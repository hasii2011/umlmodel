# Sequence Diagram Execution Specification Model Support

## Overview

In the OMG UML 2.5 specification, an **Execution Specification** (historically termed *Execution Occurrence* or *Focus of Control*, visually rendered as an *activation bar*) represents the duration in time during which a participant (Lifeline) is actively executing a behavior or action.

Currently, sequence diagram executions in `umlshapes` (`UmlSDExecution`) and `umlio` (`UmlSDExecutionsToXml`) are handled as presentation-layer shapes with visual properties (`attachedToId`, `startY`, `endY`, and `nestingLevel`). This document specifies the future domain model representation `SDExecution` in `umlmodel` to provide full semantic modeling support.

---

## Proposed Model Class: `SDExecution`

In `umlmodel`, `SDExecution` will inherit from `UmlModelBase` (consistent with `SDInstance` and `UmlModelBase`).

```python
from dataclasses import dataclass
from typing import Optional
from umlmodel.UmlModelBase import UmlModelBase
from umlmodel.SDInstance import SDInstance
from umlmodel.SDMessage import SDMessage

@dataclass
class SDExecution(UmlModelBase):
    """
    Data model representation of a UML Sequence Diagram Execution Specification.
    Represents a period of active control or processing on an instance lifeline.
    """
    instance:      SDInstance
    startTime:     int                  = 0
    endTime:       int                  = 0
    nestingLevel:  int                  = 0
    operation:     Optional[str]        = None
    startMessage:  Optional[SDMessage]  = None
    finishMessage: Optional[SDMessage]  = None
```

---

## Attribute Specifications & OMG UML 2.5 Rationale

### 1. `instance: SDInstance` — **Mandatory (Not Optional)**
* **OMG UML Specification:** `ExecutionSpecification.covered: Lifeline[1]` specifies a strict multiplicity of **exactly 1**.
* **Rationale:** An execution occurrence cannot exist in a vacuum; it physically and semantically represents active execution on a specific participant's lifeline. Therefore, `instance` is a required non-null parameter.

### 2. `startTime: int` & `endTime: int` — **Mandatory Coordinates**
* **OMG UML Specification:** An `ExecutionSpecification` is bounded by two `OccurrenceSpecification` events: `start` and `finish`.
* **Rationale:** Represents the logical time step boundaries along the lifeline coordinate axis.

### 3. `nestingLevel: int` — **Mandatory Depth (Default: `0`)**
* **Rationale:** Represents the horizontal visual displacement and execution call depth for overlapping, nested, or re-entrant activations on the same lifeline.

### 4. `operation: Optional[str]` — **Optional**
* **OMG UML Specification:** UML 2.5 distinguishes between:
  - *`ActionExecutionSpecification`*: An execution specification representing the execution of an explicit `Action` (such as a `CallOperationAction` referencing a class method).
  - *`BehaviorExecutionSpecification`*: An execution specification representing direct behavior execution without requiring a named class operation.
* **Practical Modeling Rationale:**
  - In early analysis sketching or high-level architecture diagrams, developers routinely draw activation bars without binding them to a named method.
  - Activations often represent internal computation, script execution, or background processing rather than a defined class method.

### 5. `startMessage: Optional[SDMessage]` — **Optional**
* **OMG UML Specification:** The start boundary is an `OccurrenceSpecification` (`ExecutionStartEvent`). While typically paired with a `ReceiveMessageEvent` from an incoming message, this linkage is not mandatory in the metamodel.
* **Practical Modeling Rationale:**
  - **Autonomous / Initiating Participants:** The initial participant in a sequence diagram (e.g., an `Actor`, a daemon thread, a batch process, or an interactive UI button event) starts executing spontaneously without receiving an incoming message first.
  - **In-Progress Diagram Editing:** In a diagramming tool, a user may create an activation bar on the canvas before routing an incoming message link to it.

### 6. `finishMessage: Optional[SDMessage]` — **Optional**
* **OMG UML Specification:** The finish boundary is an `OccurrenceSpecification` (`ExecutionEndEvent`). It does not require a paired `SendMessageEvent` (reply).
* **Practical Modeling Rationale:**
  - **Asynchronous Messaging:** In asynchronous or fire-and-forget communication, a method executes and completes without ever transmitting a return message.
  - **Void Returns:** In standard sequence diagram practice, explicit return messages (`<--`) are frequently omitted for void methods to reduce visual diagram clutter.
  - **Abrupt Termination:** An execution occurrence may terminate due to an unhandled exception or process termination without returning a message.

---

## Why Model Support Is Needed for Future Capabilities

1. **Semantic Validation & Integrity:**
   - Enables diagram validation rules ensuring that execution occurrences belong to valid instances, are within lifeline temporal bounds, and are properly ordered.
   - Allows validating that when a synchronous message targets a lifeline, a corresponding execution specification exists.

2. **Code Generation & Call Stack Synthesis:**
   - Sequence diagrams serve as behavioral blueprints. Having `SDExecution` linked to an `SDInstance` and `operation` allows automated code generators to reconstruct call stacks, method invocations, and synchronous wait blocks.

3. **Round-Trip Model Interchange & XMI Export:**
   - Standard OMG UML 2.5 interchange formats (XMI) require behavioral `ExecutionSpecification` elements (`ActionExecutionSpecification` / `BehaviorExecutionSpecification`) linked to `Lifeline` and `OccurrenceSpecification` events.
   - Having `SDExecution` in `umlmodel` enables lossless export to standard UML modeling tools (e.g., Enterprise Architect, MagicDraw).

4. **Consistency Across `umlio` Serializers:**
   - In `umlio`, `<UmlSDInstance>` wraps `<ModelSDInstance>`, and `<UmlSDMessage>` wraps `<ModelSDMessage>`.
   - Introducing `SDExecution` will allow `<UmlSDExecution>` to wrap a `<ModelSDExecution>` element, unifying the serialization and deserialization architecture across all sequence diagram shapes.

5. **Timing, Latency, and Concurrency Analysis:**
   - Modeling execution occurrences semantically allows computational analysis of message processing durations, synchronous blocking periods, and thread concurrency across distributed participants.
