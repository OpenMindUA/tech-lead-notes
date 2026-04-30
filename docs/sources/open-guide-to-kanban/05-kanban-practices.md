---
title: Kanban Practices
source_id: open-guide-to-kanban
chapter: Kanban Practices
chapter_index: 5
source_url: "https://kanbanguides.org/open-guide-to-kanban/"
source_version: v2025.7 (July 2025)
license: CC-BY-SA-4.0
authors: John Coleman, Magdalena Firlit, Nigel Thurlow, Jose Casal, Martin Hinshelwood, Andy Carmichael, Jim Benson, Michael Forni, Christian Neverdal, Nader Talai, Steve Tendon
tags: [kanban, open-guide-to-kanban, kanban-practices]
---
## Kanban Practices

### Defining and Visualizing the Workflow

Optimizing *Flow* requires defining what *Flow* *of Value* means in a given context, *the (ideally) smooth movement and delivery of potential or (ideally) realized benefits for Stakeholders*. The explicit shared understanding of Flow among Kanban system members within their context is called a Definition of Workflow. *Definition of Workflow* is a fundamental concept of Kanban. All other elements of this guide depend heavily on how workflow is defined.

*To inform optimal workflow operation and facilitate continuous improvement, at a minimum*, Kanban system members must create their *Definition of Workflow* using all of the following elements:

1. A definition of the individual units of Value that are moving through the workflow, referred to as *Work Items (or Items)*.
2. *Depending on the Work Item, for at least one coherent ‘started’ and ‘finished’ point pair:*
   - One or more defined states that the *Work Items* *Flow* through from ‘started’ to ‘finished.’
   - *Work Items* between the ‘started’ and ‘finished’ points, even if waiting in a Queue or Buffer, are considered:
     - *‘Started but Not Finished Work’ (SNFW) or*
     - *Work in Progress*/*Process* (WIP).
   - A definition of how WIP will be controlled from ‘started’ to ‘finished.’
   - *A set of* Explicit policies about how *Work Items* can *Flow* through each state from ‘started’ to ‘finished’ *defect-free*. *For example, Kanban system members might have a policy that is explicit about fixing any known defects in an Item before moving it to the next state, so that no known defect is passed to a subsequent process.*
   - A *Service Level Expectation* (SLE): A forecast of how long it should take a *Work Item* to *Flow* from ‘started’ to ‘finished.’ *Note that there is no guarantee that what happened in the past will happen in the future.*
   - A *Visualization* of the *Service Level Expectation* on the Kanban board.

The order in which these elements are implemented is not important as long as they are all *implemented*. Kanban system members often require additional *Definition of Workflow* elements, such as values, principles, and working agreements, depending on the *circumstances of the* Kanban system *members*. *There are resources in the appendix of this guide and elsewhere to help decide on appropriate options*.

Kanban system members also often require more than one *Definition of Workflow*. Those multiple *Definitions of Workflow* could be for multiple groups of Kanban system members, different levels of the organization, etc. While this guide prescribes no minimum or maximum number of *Definitions of Workflow*, it encourages establishing a *Definition of Workflow* wherever the Kanban system members require connecting *Flow* to *Value*.

*Enabling Flow is the act of fostering a smooth and balanced system to create Value. The Definition of Workflow should ensure that the system is balanced to optimize the Flow of Value. Kanban system members accomplish this by improving how they validate that Value was delivered, and eliminating Work that fails to deliver Value.*

The *Visualization* of one *or more* *Definitions of Workflow* is *described as* a Kanban board. There are no specific guidelines for how a *Visualization* should look. Consideration should be given to all aspects of a *Definition of Workflow* (e.g., *Work Items*, policies) along with any other context-specific factors that may affect how Value *Flows*.

*In a software team, Kanban might Visualize feature development from idea to deployment. In a marketing team, it might track a campaign from design to launch.*

Kanban system members are limited only by their imagination regarding how they make *Flow* *visible and how they foster purposeful and intentional interactions with the right people at the right time*. *It is recommended to Visualize each step in a workflow to prevent waste from remaining hidden.*

### Actively Managing Items in a Workflow

Items in the workflow must be actively managed. *Active management of Items in a workflow can take several forms, including, but not limited to, the following:*

- *Control* ‘*Started but Not Finished Work’ (SNFW) or Work In Progress/Process (WIP)*.
- *Ensure* *Work Items* do not age unnecessarily, using the *Service Level Expectation* as a reference.
- *Resolve impediments that are causing blocked Work or blocked processes*.

A common practice is for Kanban system members to review the active *Items* *on a regular basis*. This review can occur continuously or at regular intervals. Kanban system members must explicitly control the number of *Work Items* in a workflow from ‘started’ to ‘finished,’ directly or indirectly. That control can be represented on a Kanban board in any way that *Kanban system* members deem appropriate.

*The use of WIP limits (16) in Kanban for Knowledge Work typically indicates that demand can exceed the team’s capacity, so WIP limits (16) are used to regulate and balance the Flow of Work Items and prevent overload.*

*In contrast, a Toyota just-in-time (JIT) pull system prevents demand from exceeding supply, as subsequent requests will not be serviced until the previous one has been fulfilled—a self-limiting or self-regulating system designed to synchronize production with actual customer demand and minimize inventory in a stable, predictable manufacturing environment.*

*Making only what is needed just-in-time is the cornerstone of the Toyota Production System. The Kanban system in the Toyota Production System pulls exactly what is needed when it is needed.*

For Knowledge Work, Kanban system members should start Work on (*select*) an Item only when there is a clear signal that there is capacity to do so. When WIP drops below the control set in the *Definition of Workflow*, that can be a signal to select new work. Kanban system members should refrain from selecting more *Work* into a given part of the workflow *beyond the relevant WIP control(s)* *or selecting Work greater than their capacity. When needed, the Work should be split into smaller yet still potentially valuable Items.*

*There is no requirement to have a repository of Work Items that are not yet Work In Progress/Process, often referred to as a backlog. A backlog is emergent and can include various stages or aspects of Work preparation. If there is one, there is no need for it to be in a list format or sequenced.*

*Ideally, Work should enter the Kanban system guided by policies rather than being assigned to an individual. In the pursuit of managing idle work, not idle people:*

- *The Kanban system members should self-organize around the Work and Definition of Workflow.*
- *Kanban system members should ‘start’ Work when they are ready to work on it, bringing in new Work based on how it is being prioritized.*
- *Kanban system members––and others outside the Kanban system––should explicitly prevent Work from being pushed to Kanban system members.*
- *Beware of re-prioritization of ‘Started but Not Finished Work’ (SNFW) or*  
  *Work In Progress/Process (WIP), as it causes those Items to age (sit idle)*  
  *and leads to longer or less predictable Elapsed Times from ‘Started’ to ‘Finished.’*

*Rightsizing, an optional but recommended practice, refers to assessing whether Work Items fit the Service Level Expectation, or are too big for the Service Level Expectation and therefore require splitting into smaller but still potentially valuable Work Items.*

*Rightsizing, in a Knowledge Work context, is based on the assumption that Work Items need to be at or under a maximum size (according to the Kanban system members) but do not necessarily need to be the same size. If a Work Item is so large that it can’t be completed within a reasonable time (e.g., it would break the Service Level Expectation), even after starting it, Kanban system members should consider splitting it into smaller Items that each have the potential to deliver Value. Equally, Work Items can be merged.*

*Capacity management often requires more than WIP control.* Controlling WIP helps *Flow* and often improves the collective focus, commitment, and collaboration *of the Kanban system members*. Any acceptable exceptions to controlling WIP should be *explicitly stated* as part of the *Definition of Workflow*.

### Improving *Flow*

Given an explicit Definition of Workflow, it is the Kanban system members’ responsibility to continuously improve their *Flow* *by* *achieving* a better balance of effectiveness, efficiency, and predictability. Continual study of the system can guide potential improvements. *Kanban system members often review* the *Definition of Workflow* to discuss and *adopt* *needed* changes.

*Improvements are* *often* *just-in-time*. *Improvements are not limited by their size or scope. Sometimes, improvement is beyond the control or influence of Kanban system members. Purposeful and intentional interactions, cultivating change, and removing Blockers at all levels are key to improvement.*

*Better still, people who demonstrate leadership, also known as leaders, Go See, Listen, and really understand to collect the facts to inform decision-making. This is known as Genchi Genbutsu. Leaders do Genchi Genbutsu so often that the truth emerges. Knowledge of what to do is one thing, but purposeful, relentless, iterative, compassionate action toward improvement (incl. shorter feedback loops) is another.*

*Kanban favors evolutionary change, but it does not prohibit larger, structural changes, informed by evidence and a clear understanding of the system. Changes should be purposeful and context-driven.*
