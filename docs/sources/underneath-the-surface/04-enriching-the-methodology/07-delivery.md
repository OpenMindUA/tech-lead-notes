---
title: Delivery
chapter: Enriching the Methodology
chapter_index: 4
section: Delivery
section_index: 7
source_url: "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"
source_date: 2023-06-08
source_lines: 1557-1638
license: CC-BY-4.0
author: Nader K. Rad
tags: [enriching-the-methodology, delivery, performance-domain]
---
## Delivery

There’s the story that a manufacturer of elevators had complaints that their elevators were too slow. They ran multiple projects to improve their speed, with different levels of effectiveness, but the complaints remained. At one point, they wanted to initiate a new project to increase speed, and someone responsible in that project asked a fundamental question:

A: Why?  
B: Why what?  
A: Why do you want to make it faster?  
B: Because the users and customers want it to be faster.  
A: Why do they want it to be faster?  
B: I don’t know… I suppose faster is better!  
A: Why is it better?  
B: Well… it’s a small box and people don’t have anything to do there, so they just get bored.  
A: So, the goal is to prevent boredom rather than to increase speed!

So they added a mirror to the elevator! It kept people busy looking at themselves, and the interesting point is that they even thought the elevators had become faster, although it was at the same speed as before.


### Start with requirements

It’s always risky to rush into the first “obvious” solution without staying with the problem long enough. That’s why we have a certain process:

Requirements → Deliverables → Activities

Many plans start with activities or deliverables. Ideally, though, we want to start with requirements, then use the requirements to design the deliverables, and finally, see which activities are needed for building those deliverables.

This process is the same for predictive and adaptive projects. The difference is that most requirements are identified at the beginning of a predictive project, but must be identified gradually during an adaptive project.

So, what would you do if someone told you, in the middle of an IT development project, that they need to have a feature for the support staff to be able to log in as different users without having the passwords of those users?

What they’ve described is a deliverable, and you must ask questions to understand what the requirement is behind this deliverable. When you find the requirement, check to see whether there are other solutions for it, and which one would work best.

The traditional approach in adaptive projects, mainly created in XP (eXtreme Programming), is to describe what they want as a *user story*, or *story* for short. There are different ways of forming a story, and the modern way goes something like this:

> As a member of support staff, I want to be able to log in as any user without having their password so that I can check what they see from their side and try to solve their problems (e.g., missing an order) instead of asking them lots of questions or expecting them to send screenshots.

This format contains a reason at the end that works like a requirement and encourages everyone to think about it. Besides that, it helps reinterpret the request; for instance, in the example above, we can see that they wouldn’t need to log in as high-privilege admin users (that would be a bad idea) and it’s best to make that clear right away.

Is this concern explicit enough in your methodology? If not, you may need to do something about it appropriate to the size and complexity of the project.


### Deliverable breakdowns

Another topic related to deliverables is that most projects have too many deliverables, and it would be overwhelming if you tried to manage them in a flat list. For this reason, most methodologies use hierarchical breakdowns for deliverables, where the project is broken down into a few major elements, and those into their building elements and so on for a few more levels until you reach the level of detail required for the project. Many resources call it a *work breakdown structure* (WBS), but other names are common as well; for example, PRINCE2® calls it a *product breakdown structure* (PBS) and P3.express calls it a *deliverables map*.

Small projects can manage their deliverables with a flat list; for instance, micro.P3.express, which is designed for micro projects, doesn’t have a mandatory *deliverables map*. However, larger projects can benefit a lot from having a hierarchical breakdown of deliverables. If you have such a project and your methodology doesn’t have one (e.g., most Agile methods), you may need to add one.


### When to deliver

Sooner or later, the final output of the project, including all its *deliverables* will be delivered to the customer and the end users. The when and how of this depends on many factors:

- **Predictive projects:** Because of the more-or-less linear development in predictive projects, their outputs are usually not usable until the end of the project. (Think of a project for building a bridge.) Therefore, the output is usually delivered in one go, at the end of the project. On the other hand, some predictive projects may have major phases that end at different times and create usable subsets of the final output, and therefore, it may be possible to deliver them in a few steps instead of all together at the end.
- **Adaptive projects:** Adaptive projects create usable *increments* of the final output throughout the project to collect feedback and guide the way forward. These increments can be released to production and used by real end users, but when it’s not possible (because of the operations difficulties), they will be given to subsets of end users, or even representatives of them. In this way, their delivery *can* be continuous.

An *increment* of the output is a set of *deliverables* that are *usable* by the end users; i.e., every increment is a set of deliverables, but not every set of deliverables is an increment. Projects can’t be adaptive unless they have *incremental delivery*, because useful feedback can only be generated by something usable, and not with other sets of deliverables that may be too abstract for typical users to understand.


### Delivery risk

Having only one delivery at the end of the project is risky in all situations, because if something is not the way the customer and end users expected, it will be costly to fix the problem. Therefore, even in predictive projects where we may not have true deliveries throughout the project, we still prefer to review deliverables with the customer and end users and receive their formal or informal approval. This is usually embedded in methodologies, but if not, and you can predict problems for the delivery at the end of the project, it’s best to adjust your methodology.


### Limiting work in progress

Limiting work in progress is an essential concept in *lean* manufacturing, which has had a great impact on Agile methods. However, it’s not limited to adaptive projects, and every project can benefit from it.

We don’t have to avoid all forms of parallel work, but there’s an optimal level of parallelism for each type of work that is usually much lower than what most people expect. When you spread your capacity into too many deliverables at the same time, it becomes too distracting, and everyone would be tempted to start working on a new deliverable as soon as one runs into difficulties. Solving issues and finishing something immediately is usually easier than leaving it for the future. Remember: It’s best to focus on finishing everything sooner rather than starting it sooner.

It’s helpful to have an element in your methodology that encourages everyone to finish and close deliverables before moving on to new ones. On the other hand, the same element can be connected to an informal (or formal, if needed) acceptance by the project manager and then by the customer, which in turn helps with the previous point about avoiding issues at the end of the project.


### Quality of work

So, it’s a good idea to have a process for the project manager to check completed deliverables and give their informal approval. However, how can a project manager do so when they are not a technical expert?

This control is focused on making sure the deliverable satisfies its requirements and expectations. That can be translated into scope and quality. Before starting the work, you get help from technical experts to define the scope and quality of the deliverable and make sure they are aligned with the requirements and expectations. When the work is finished, you then *help* those technical people by reviewing their work based on the definitions to make sure nothing has been missed.

To be able to do so, you need to define scope and quality upfront, or at least just before work on each deliverable starts. For example, PRINCE2® has an artifact called *product description* for this purpose, and P3.express uses comments in its *deliverables map* to store the information. Check your methodology to see how it’s done and whether or not it’s appropriate for your project; if not, tailor it by increasing or decreasing the level of detail and formality, turn it into a separate artifact, or merge it into an existing one, etc.

Agile projects usually involve writing down the items on sticky notes or index cards. One side can contain the user story while the other side contains the extra information about acceptance criteria. On the other hand, many of the items in IT development projects have similar acceptance criteria, and therefore, instead of repeating them, we can extract those common criteria and store them in a single element. That element is called a *definition of done* in many Agile systems.
