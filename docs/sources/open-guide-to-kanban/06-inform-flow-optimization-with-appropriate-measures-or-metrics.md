---
title: Inform Flow Optimization with Appropriate Measures or Metrics
source_id: open-guide-to-kanban
chapter: Inform Flow Optimization with Appropriate Measures or Metrics
chapter_index: 6
source_url: "https://kanbanguides.org/open-guide-to-kanban/"
source_version: v2025.7 (July 2025)
license: CC-BY-SA-4.0
authors: John Coleman, Magdalena Firlit, Nigel Thurlow, Jose Casal, Martin Hinshelwood, Andy Carmichael, Jim Benson, Michael Forni, Christian Neverdal, Nader Talai, Steve Tendon
tags: [kanban, open-guide-to-kanban, inform-flow-optimization-with-appropriate-measures-or-metrics]
---
## Inform Flow Optimization with Appropriate Measures or Metrics

- **Blocked Elapsed Time for Finished Items (BETFI):** The cumulative time for a single ‘finished’ Work Item (or a selection of ‘finished’ Items) spends in a blocked condition from ‘started’ to ‘finished,’ but not in a Queue or Buffer state. [measure for a single Item, metric for multiple Items]

- ***Cumulative Queueing or Buffer Time (CQBT):*** *The cumulative time a ‘finished’ single Work Item (or a selection of ‘finished’ Items) spends in Queueing or Buffer states from ‘started’ to ‘finished.’ [measure for a single Work Item, metric for multiple Work Items]*
- ***Elapsed Time from ‘Started’ to ‘Finished’ (ETSF):*** The (typically *rounded-up) number of elapsed time units (often calendar days) from* when a single *Work Item* ‘started’ *to* when a *Work Item* ‘finished.’ *Only ‘finished’ Items get ETSFs. [measure]*
- **Flow Distribution:** The Visualization and analysis of Work Item types ‘finished’ or ‘completed’ over time, enabling active management to ensure a healthy balance of effort. [metric]

- ***Flow Efficiency:*** The ratio of active working time to the total time an Item or a selection of Items spends in the workflow, including waiting times, between the ‘started’ and ‘finished’ points on a Definition of Workflow. *It is expressed as a percentage. It can be misleading, as time spent in active states may not be actual active time. ((ETSF-(CQBT+other non-value-adding time))/ETSF) 100. [metric] Example of other non-value-adding time: Blocked Elapsed Time for Finished Items*
- **Number of Blockers:** The number of impediments, partial or complete, at a given point in time (usually current datetime), to the Flow of Work Items from ‘started’ to ‘finished.’ [measure]
- **Process Cycle Efficiency:** Measures the Work efficiency of a system or its parts. It is calculated by dividing Value-adding time by Time to Market and then multiplying by 100 to get a percentage. This means Kanban system members have to measure all Value-adding and all non-Value-adding time (including, but not limited to, waiting time). ((T2M-(CQBT+other non-value-adding time))/T2M) 100. [metric]
- ***Service Level Expectation:*** A forecast of how long it should take a *Work Item* to Flow from ‘started’ to ‘finished.’ The *Service Level Expectation* itself has two parts: a period of elapsed time and a probability associated with that period (e.g., ‘85% of *Work Items* will be ‘finished’ in eight days or less’). *It is based on a selection of Elapsed Time from ‘Started’ to ‘Finished’ from all history, a subset of history, or if data does not exist or is insufficient, an educated guess. [metric]*
- **‘Started but Not Finished Work’ (SNFW)** or **Work In Progress/Process (WIP)** *or **Flow Load***: *The* number of *Work Items* ‘started’ but not ‘finished’. *[measure]*
- **Throughput:** The number of *Work Items* ‘finished’ per unit of time. The measurement of throughput is the exact count of *Work Items*, *not revenue. [metric]*
- **Time to Market, also known as Customer Lead Time:** The (typically rounded-up) number of elapsed time units (often calendar days/weeks) from when a Stakeholder’s order for a single Work Item was received to when the Work Item was delivered to the Stakeholder. It is one example of an ETSF. [measure for a single Work Item, metric for a product or service]
- **Total Work Item Age (TWIA)** or **Total Elapsed Time for ‘Started’ but Not ‘Finished’ Items (TETSNFI)** **:** The total elapsed time from when all in-progress (‘started’ but not ‘finished’) Work Items ‘started’ to a specified datetime, usually the current datetime. [metric]
- **Work Item Age (WIA)** or ***Elapsed Time for ‘Started’ but Not ‘Finished’ Items(ETSNFI)*** : The (typically *rounded-up) number of elapsed time units (often calendar days)* *from* *the datetime a single ‘not finished’ Work Item* ‘started’ *to* *a specified datetime, usually the current datetime. By acting on relatively older Items, feedback loops can be shortened, and Flow improves. [measure]*

The *Flow* metrics *and measures* apply to the appropriate ‘started’ and ‘finished’ points established by the Kanban system members in their *Definition of Workflow*. *If there are multiple sets of ‘started’ and ‘finished’ points, some flow metrics and measures are often applied to each ‘started’ and ‘finished’ pair.*

***If Kanban system members are unsure where to start, this guide suggests:***

*Time to Market, and for each coherent ‘started’ and ‘finished’ pair:*

- *A Service Level Expectation (required for at least one ‘started’ and ‘finished’ pair),*
- *Work Item Age or Elapsed Time for ‘Started’ but Not ‘Finished’ Items (ETSNFI),*
- *Elapsed Time from ‘Started’ to ‘Finished’ (ETSF), and*
- *Throughput.*

Provided that Kanban system members use *Flow* metrics *and measures* as described in this guide, *and they are appropriate for the context,* they can refer to any of them by other names. It is up to the Kanban system members to decide how best to *use* these *Flow* metrics *and measures, such as Visualizing them in charts or assessing variation. A proactive focus on outcomes, impact, and Value is recommended.*

### *Outcomes, Impact, and Value*

*Kanban system members should regularly look for evidence of outcomes/impact, e.g.:*

- *Customer outcomes could focus on delivering measurable Value to customers, e.g., reduced Failure Demand, customer long-term cost reduction, or addressed customer jobs (18).*
- *User outcomes could address specific changes in user behavior that solve problems or improve experiences, e.g., ‘completing’ Work Items more effectively at the lowest costs, or better usability.*
- *Product Stakeholder outcomes could connect these behavioral changes to product performance metrics, such as trends in product customer adoption, retention, and convergence, as well as trends in feature adoption, decision-maker and user metrics, and product Time to Market.*
- *Business Stakeholder Impact, e.g., compliance, business long-term cost reduction, business results, trends in market share, customer satisfaction across all products, etc.*
- *Outcomes for Kanban system members such as improved capability, considering for example, psychological flow (15), frequency of release, tooling, skills, technical debt, user experience (UX) debt, customer experience (CX) debt, human-centered-design debt, technical domain capability, market domain capability, business domain capability, and a climate/culture for net improvement.*

Any of the above approaches can be useful. Also, consider the following:

- **Failure Demand** (17)**:** Demand caused by a failure to do something or do something right for the customer. It is a signal for potential improvement. It highlights where capacity is being wasted due to previous failures, poor Work, or bad decisions. For example, a customer support team may receive repeated calls due to unclear billing instructions. [metric]
- **Time to Validated Value, also known as Time to Value or Time to Outcome:** The *rounded-up number of elapsed time units (often calendar days/weeks) from when a Stakeholder’s order for a Work Item was received to when Value was validated. It is one example of an ETSF focusing on valuable and measurable outcomes. [measure]*
- **Value Validated:** A Work Item that reaches the ‘finished’ point and delivers the intended Value to the Stakeholder (including, but not limited to, customer or user), meeting explicit policies, e.g., quality or experience standards. Often includes evidence and observations.
- **Value Invalidated:** A Work Item that reaches the ‘finished’ point or is evaluated but fails to deliver the intended Value, not meeting expectations defined in the Definition of Workflow, often requiring rework or rejection, informed by evidence and observations. Consider the context.

*By measuring these kinds of outcomes, impacts, Value metrics, and Value measures, Kanban system members ensure they’re not just delivering Work quickly (outputs), but delivering real Value and improvements (outcomes and impacts) to Stakeholders, including but not limited to customers and users.*

*Clarity and understanding of Work Items should happen just-in-time to avoid waste.* Avoid excessive focus on outputs and insufficient focus on outcomes. *Kanban system members should proactively, intentionally, purposefully, and regularly review the metrics or measures and continually improve them.*
