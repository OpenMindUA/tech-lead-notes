---
title: DSDM®
chapter: Selecting a Methodology
chapter_index: 3
section: DSDM®
section_index: 4
source_url: "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"
source_date: 2023-06-08
source_lines: 1030-1092
license: CC-BY-4.0
author: Nader K. Rad
tags: [selecting-a-methodology, dsdm, methodology]
---
## DSDM®

DSDM is another first-generation Agile method. In contrast to Scrum and other systems of the time, it was created from the ground up to be compatible with large, complicated IT development projects with multiple teams. Its structure is inspired by PRINCE2®.


### Team structure

DSDM® has an interesting, though relatively complicated team structure:

- **Project Level:** This contains a number of roles responsible for the overall project outputs/outcomes and coordinating the teams.
  - **Business Sponsor:** This is the most senior role in the project, responsible for its justification, budget, etc.
  - **Business Visionary:** They interpret the business needs at the project level.
  - **Project Manager:** They are responsible for the day-to-day management of the project.
  - **Technical Coordinator:** They are responsible for coordinating the technical aspects of the project across teams.
- **Solution Development Team Level:** There can be one or more teams, each with a number of roles required for coordinating themselves with the project level, making decisions within their threshold, and producing the output.
  - **Team Leader**: They are responsible for the management aspects inside the team, and they are in touch with the Project Manager.
  - **Business Ambassador:** They bring their business and user expertise to the team, and they are in touch with the Business Visionary.
  - **Solution Developer:** They are the people who build the product.
  - **Solution Tester:** They help ensure the quality of the product.
- **Support Level:** This contains a number of roles that support multiple teams.
  - **Technical Advisor:** They help teams in certain technical aspects; e.g., security.
  - **Business Advisor:** They help teams by providing them with business and user information; e.g., legal and regulatory aspects
  - **DSDM Coach:** They help teams understand how to use the DSDM methodology.
  - **Workshop Facilitator:** They help everyone by facilitating their workshops.

In addition to the roles above, there’s also a *Business Analyst* role that belongs at both the project level and the team level. They have both business and technical knowledge and bridge the gaps between them.


### Process

A DSDM® project starts with a *pre-project* phase to evaluate the project and decide whether or not to invest on it. The output will be stored in an artifact called the *Terms of Reference*.

If the decision is made to proceed with the project, the *feasibility* phase is then run. During this phase, we’ll spend more time on the business, technical, and managerial aspects of the project and create a *feasibility assessment* artifact, which will be used to decide whether it’s a good idea to go even further.

The next phase is *foundations*, which puts more effort into the same areas targeted during *feasibility* to create a foundation for the project (i.e., a high-level plan). The output will be stored in the *foundations summary* artifact. If needed, this phase can be repeated in the project to refine the foundation.

After creating the foundation, we proceed with the *evolutionary development* phase. We have many cycles of this phase, and for each, we detail the foundations to create a plan for the cycle, and at the end, create a new *increment* of the product.

There’s also a *deployment* phase, which may run with the same frequency as *evolutionary development*, or a lower one. Each time it’s run, it puts the latest *increment* into production for the end users. In general, we prefer to have as many deployments as possible, because that makes adaptation easier; however, that can be limited by business requirements, risk of disturbing the users, etc. There’s an optimum deployment ratio that depends on the type of product.

A form of closure is implied in the *deployment* phase, and therefore, there’s no separate closure phase for the whole project. However, there’s a *post-project* phase for evaluating the benefits of the project after it’s finished.

DSDM projects are timeboxed, meaning that the whole project ends exactly as defined upfront, and during that time, we try to deliver as much as possible. DSDM® heavily depends on using the *MoSCoW prioritization* technique to support this method.

MoSCoW stands for the following:

- **(M)ust-have items:** Items we must have in the product, because without them the product will be unusable (e.g., security for a banking application).
- **(S)hould-have items:** Items we should have in the product as we’d run into problems without them. However, we can have workarounds for those problems (e.g., doing the task manually).
- **(C)ould-have items:** Items that would be nice to have and would add value, but whose absence won’t cause problems (e.g., having a dark theme in the banking app).
- **(W)on’t have this time:** Items we decide to exclude.

In the beginning, during the *feasibility* and *foundations* phases, we create a list of items along with their priorities and order them. The list is called the *prioritized requirements list*. The items are high-level at the beginning, and we break them down into smaller items as we proceed, especially when detailing the plan for development iterations.

To have enough flexibility in the project, we should have no more than 60% must-have items and no less than 20% could-have items. When estimating the fixed duration of the project,

- we must have enough time to finish everything in an optimistic way, and yet
- we should be able to deliver all the must-have items within our most pessimistic estimates.

When working on the project, our progress measurement will be focused on checking how many items we can finish by the end of the project. If, at any time, we forecast that we can’t deliver all the must-have items, we should probably cancel the project, or at least make fundamental changes.

Basically, we guarantee that we’ll deliver all the must-have items, we’ll do our best to deliver all the should-have items, and we’ll see what we can do about the could-have items.
