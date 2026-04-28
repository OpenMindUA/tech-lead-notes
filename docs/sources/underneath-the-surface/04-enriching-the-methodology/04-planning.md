---
title: Planning
chapter: Enriching the Methodology
chapter_index: 4
section: Planning
section_index: 4
source_url: "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"
source_date: 2023-06-08
source_lines: 1360-1442
license: CC-BY-4.0
author: Nader K. Rad
tags: [enriching-the-methodology, planning, performance-domain]
---
## Planning

We were late for a meeting. We got into the car to go, and I started setting my GPS navigation and checking various routes. My companion told me, “Come on, let’s go, we’re too late, we don’t have time for that!” But I was doing it exactly because we didn’t have enough time. A delay of less than a minute for planning could save us a lot of time later on by selecting the fastest route.


### Planning for different development approaches

All projects need planning, with no exception. Some people think that Agile project don’t need planning, which is not correct. They just have a different type of planning:

- **Predictive** projects have either a detailed or a high-level plan upfront. When the upfront plan is high-level, there would be cyclic (e.g., monthly) stages for detailing them.
- **Adaptive** projects have a really high-level plan upfront. Some level of detail may be added on various cycles during the project, but each element is fully detailed only before it’s executed.

Anything we do must have a purpose. We don’t plan for the sake of planning, but we do so to

1.  direct the project, and
2.  enable monitoring and controlling.

The first of these depends on the development approach while the second depends on the project management methodology. That’s why planning is not an isolated concept and why we can’t judge how good a plan is without checking the development approach and the management methodology. Something that might be a good plan in one setup may not be so in another.


### Continual planning

Planning is a *continual* activity, and regardless of the type of upfront planning, we **must** continually replan. Some people think they can spend a couple of weeks upfront creating a schedule, print it on a large piece of paper and put it on the wall, and then they are fine for the whole duration of the project. A plan that is created once and never revised cannot be of any use, though.


### The subject of planning

When and how to plan is usually covered well in all methodologies, but the subject of planning is something you can spend more time on and tailor to your project when needed.

The old versions of the PMBOK Guide had a set of *knowledge areas* that were similar in some aspects to our current topic of performance domains, yet mainly different. They are, in my opinion, the best way of explaining various subject areas for planning as well as monitoring and controlling. Here are the old knowledge areas:

- Integration
- Scope
- Schedule
- Cost
- Quality
- Resources
- Communications
- Risk
- Procurement
- Stakeholders

This is only a way of structuring what you already know about various areas, but it’s a well-formed list you can use to double-check and make sure everything is covered properly in your system. Your method probably covers all of them, but the level of detail may not be suitable for your project. So, the next time someone shows you a time schedule and says that it’s their “plan”, show them the list above and ask them where the other 12 areas are planned!


### Types of schedule

Planning covers cost, quality, scope, risk, and many more areas. A core concept that should be planned for is time, which we usually refer to as a *schedule*. Scheduling is assigning time or order to the elements.

There are two main forms of scheduling:

- Dependency-based
- Priority-based

In many projects, there are hard, unavoidable dependencies among elements; for example, you can’t paint a wall before building it, and you can’t build it before building the floor underneath it. Such projects are usually scheduled using a dependency-based method, where we create a network of those dependencies along with other determining factors and use that to calculate the orders and start dates. This calculation is done using either the *critical path method (CPM)* or a method similar to it.

Software applications such as Oracle’s Primavera P6 and Microsoft Project are examples of tools built around the CPM methods.

On the other hand, some projects can be broken down into building elements that are not too dependent on each other. In this case, you don’t need a dependency-based schedule, and a simpler priority-based method would suffice. In this method, you assign a priority to each element and then order them based on their priorities and importance, and then work through the list.

Adaptive projects *require* priority-based schedules, and if you believe that you can’t create a true priority-based schedule, it may be a sign that the product can’t be developed using an adaptive method. Predictive projects, on the other hand, can have either type of schedule.


### Levels of planning

There are two major forms of planning:

- Planning the work
- Planning how to plan, monitor, and control the work

We can call them plans and *meta-plans*. For example, your plan for risks is a list of risks you’ve identified and your responses to them. The whole plan can be a spreadsheet called the *risk register*. Your meta-plan for risk would be a text document that describes the way you want to manage risks: the techniques you would use, the workflows, the artifacts, etc.

Each methodology tells you how to do each of these, and as such, some form of meta-plan is embedded into your methodology. However, it may not contain all the information you need in practice, and that’s why some resources recommend creating these meta-plans to complement the methodology.

Usually, the systems that expect upfront tailoring (e.g., PRINCE2®) also expect meta-plans, while those that prefer gradual, ongoing tailoring (e.g., P3.express) don’t enforce that. However, even in the second case, it would be a good idea to have them for areas that require more attention; for example, if procurement is a sensitive topic in your project, create a meta-plan for it. You can call it the *procurement strategy*, the *procurement management plan*, etc.

There are usually a lot of things in common among various projects run in an organization, and therefore, a meta-plan created in one can be usable (with some adjustments) in others. It’s best to create the meta-plans in a central place and make it available to all projects. While the projects use the meta-plans, they would adjust them, and some of the general adjustments could then be fed back to the central place to be used in future projects.

What’s described above is basically an important aspect of the first step of tailoring I explained in the principles section.

The centralized place that stores, distributes, and adjusts the meta-plan can have any name you want. A good option is a *center of excellence*. Another common term is *PMO*, which can stand for “project management office” among other things. Unfortunately, the term PMO is a vague one used for many purposes, and sometimes even has too much overlap with the project management system of individual projects, which is not a good idea.
