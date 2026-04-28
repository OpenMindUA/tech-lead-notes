---
title: Uncertainty
chapter: Enriching the Methodology
chapter_index: 4
section: Uncertainty
section_index: 8
source_url: "https://pmbok.guide/pmbok-guide--underneath-the-surface.md"
source_date: 2023-06-08
source_lines: 1639-1683
license: CC-BY-4.0
author: Nader K. Rad
tags: [enriching-the-methodology, uncertainty, performance-domain]
---
## Uncertainty

There are various topics in uncertainty, but the most important one is risk management. As we talked about before, you have a proper risk management system as long as you have a structured system for identifying, analyzing, and planning responses to risks, and then you make sure the responses are acted upon and re-analyzed.


### Level of sophistication

How you can implement a risk management system can vary widely. For example, the minimalist approach of P3.express has only one artifact called the *follow-up register*, used for storing information about risks as well as issues, change requests, improvement plans, and lessons learned. They are in the same place for two reasons:

1.  You can use a simple process that applies to all of them without making your project management system too complicated.
2.  Those elements morph from one type to another as time passes; for example, an uncertain event in the future, which is a risk, can actually occur, which then makes it an issue. When you work on it and close it, it becomes a lesson learned.

While this approach works well for most projects, a mega-project with a high degree of complexity may require a more detailed approach. In those cases, you can separate the element into different artifacts and use different processes for them.

PRINCE2® and many other resources use a separate *risk register* for storing the risk data. This register, which can be a spreadsheet, contains the analysis information as well as planned responses.

A single risk can have multiple responses, and a single response can serve multiple risks. Therefore, if you still need to make your system more advanced, it would be a good idea to separate risks and responses into two different tables and then create many-to-many relationships between them.

If you need to be even more advanced after separating out risks and their responses, you can even break the risk table into causes and effects, because a single cause can have multiple effects/risks, and each risk can have multiple causes. You can even go one step further and convert it from two tables with many-to-many relationships into a graph.

In practice, there’s no end to how complicated you can make this system, and you should always build one that is appropriate to your project. If you have doubts about the appropriate level of sophistication, though, err on the side of the simpler one.


### Quantitative analysis

Your response plans to risks must be justifiable; for example, paying €1,000 per month in insurance to avoid a low-probability event that may cost millions of euro may be justifiable, but it won’t be justifiable if the damage is only a couple of thousand euro.

Many methods leave it to you to judge the justification of responses in an intuitive or ad hoc way, and that’s fine in almost all projects. However, some sensitive projects require a more structured way of analyzing risks.

In that case, you can extract the required data and use the *Monte Carlo* analysis to combine them in various forms and give you the probabilistic outputs before and after applying the responses. For example, you may see that there’s an 85% probability of finishing your project in 22 months, whereas, if you apply the responses, which cost you €80K, you can increase that probability to 98%. Then you can check whether or not it’s worth the investment.

This type of *quantitative analysis* consumes a lot of resources and you have to make sure you really need it before adding it to your system.


### Relationships with higher management levels

Everything we do in a project should be aligned with higher levels of management, but there are different degrees of importance, and risk management is one that requires a lot of attention in this area.

The main reason for the sensitivity of risk management is that some risks impact more than one project in a company, and when they do, it’s best to respond to those risks in a holistic, unified way. To this end, you should ensure that the *portfolio management* layer of the organization maintains a list of overall risks that impact more than one project, along with their associated risk responses, and makes it available to all projects. Conversely, the list of risks from each project should be available to the portfolio management level so they can frequently review and identify risks that could impact multiple projects, and move them from the project layer to the portfolio layer.

You may be wondering what to do if your organization doesn’t have a portfolio management system. Unfortunately, there are countless problems that can arise when there’s no portfolio management layer, and there’s no solution for that other than implementing proper portfolio management! However, if you’re a project manager in an organization that doesn’t want to have a structured portfolio management system, maybe you can talk to other project managers and convince them to have monthly meetings to get together, share lessons, and talk about high-level risks across projects.

Remember that project management is about doing things right, whereas portfolio management is about doing the right things.
