  
**WHITEPAPER**

OpenTeams / Nebari Platform

**The Distributed AI Economy:**

**Intelligence Hubs, Frames, Cogs, and Ops**

*How a Three-Layer Architecture — Infrastructure, Execution, and Economy —*

*enables Context-Sharing, Capability Exchange, and a Scalable Marketplace for Owned and Accountable Intelligence*

April 2026  |  Confidential  |  Revision 4

# **Executive Summary**

The next decade of enterprise AI will not be defined by which foundation model wins a benchmark — it will be defined by which organizations successfully deploy, govern, and exchange AI capabilities as owned operational infrastructure. The shift is already underway: enterprises are moving from renting intelligence through black-box APIs to owning it through sovereign, reproducible, and auditable deployments.

OpenTeams, built on the open-source Nebari ecosystem, provides the infrastructure, abstractions, and marketplace layer that makes this shift possible at scale. This whitepaper describes the three-layer architecture at the heart of that vision, with a particular focus on how organizational context — the culture, terminology, and norms that fuel the ROI of AI — is captured, shared, and exchanged through a new class of artifacts and concepts.

* Infrastructure — Nebari, the open-source AI ecosystem including a fundamental distribution mechanism called Nebi which is used to build personalized Intelligence Hubs which encapsulate the organizational deployment of open source standards while integrating legacy applications along with AI-native workflows.

* Execution — Frames, Cogs, and Ops: Frames carry organizational context and norms; Cogs are AI workers that are oriented by those Frames; Ops are installable units that document business processes, coordinating Cogs and standardizing human oversight

* Economy — A distributed ecosystem and marketplace where Ops, Cogs, and Frames are published, discovered, installed, and exchanged across a network of Intelligence Hubs and the humans and organizations they serve

Together, these three layers create something the enterprise AI market does not yet have: a principled path from infrastructure to outcome, with an economy of context, capability, and execution that scales as the network grows. This document also identifies the essential initial interface that brings this entire system to the people who must use it — a Desktop / Web Application that lets knowledge workers in every organization combine Frames, converse with Frame-oriented Cogs, run Ops, and share organizational context with internal and external collaborators.

# **1\.  The Problem: Rented Intelligence Is Fragile, and Context Leaks Away**

Enterprise AI adoption is trapped in a paradox. Organizations understand that AI is strategically important, yet most remain dependent on vendor-controlled, black-box systems that they cannot inspect, reproduce, audit, or own. And even when they can deploy capable AI, they cannot capture and propagate the organizational context — the rules, terminology, goals, style, and norms — that turn generic AI into specialized, valuable work. The consequences result in delayed deployment of aligned and accountable intelligence across their organization.

| Failure Mode | Root Cause | Business Impact |
| :---- | :---- | :---- |
| Vendor lock-in | APIs controlled by third parties | Strategic dependency; cost unpredictability |
| Compliance exposure | Data leaves the organization | Regulatory risk in healthcare, finance, government |
| Execution opacity | No visibility into model behavior | Inability to audit decisions or reproduce results |
| Integration fragility | No standard for how AI plugs into workflows | High integration cost; frequent breakage |
| Value leakage | Capabilities cannot be shared or monetized | No mechanism for exchanging AI work |
| Context dissipation | No portable container for organizational rules, terminology, norms, skills, tools, prompts, and processes | Repetitive re-setup; brand and policy drift; context that fueled ROI does not stay with the organization that produced it |

The root cause is architectural: the market lacks a standard model for what an owned AI deployment looks like, how AI capabilities are packaged into executable units, and — critically — how the cultural and contextual knowledge of the organization is encoded, inherited, shared, and exchanged. Without these standards, enterprises cannot own intelligence. They can only rent it.

# **2\.  The Vision: A Distributed Economy of Owned Intelligence**

OpenTeams' vision is a world in which every organization — enterprise, government, research institution, or startup — deploys their own Intelligence Hubs: sovereign, governed environments  that build on the core and proprietary data of the entity,  integrates legacy applications, and then in a unified manner, runs AI capabilities completely embracing their data, with their own policies, and within their own infrastructure perimeter which may be appropriately virtualized and use private cloud instances along with edge devices.

These Hubs which provide segmented areas of integrated expertise and collaboration for each organization that deploys them do not have to remain isolated. They can connect with each other as a drawbridge connects walled castles so that appropriate derived results from the AI explorations can flow and enable coordinated collaboration as managed by the policies of the organizations that are accountable for the data they manage.   Our vision and roadmap includes at least three specific entities that can be version, managed, and exchanged across these digital pathways:

* Frames — scoped artifacts that carry organizational context, terminology, norms, skills, tool expectations, prompts, architecture, and process details.  These can be authored, inherited across scopes, and shared with internal teams or external partners

* Cogs — the potentially specialized AI workers that perform discrete tasks within an organization, oriented by the Frames that apply to them.  These can be explored, configured, specialized, and managed both within the Hub's control plane and connected to via the Desktop / Web application.

* Ops — installable, versioned programs of AI-influenced or AI-driven work.  These can be published and installed by enterprises, automating business processes that combine Cogs oriented by specific Frames and accountable to human oversight.

| The Three-Layer Thesis |
| :---- |
| Layer 1 — Infrastructure:  Nebari (the open source standard) that is drawn from to construct the Intelligence Hub (the deployment) with modular integrations reproducible via Nebi. |
| Layer 2 — Execution:  Frames (shared context) \+ Cogs (AI workers) \+ Ops (installable programs) |
| Layer 3 — Economy:  The ecosystem, community sharing mechanism, and marketplace mechanisms where Frames, Cogs, and Ops can be shared and exchanged between Hubs |
|  |
| "We don't just provide infrastructure. We define how AI context, work, and outcomes are packaged, executed, and exchanged." |

# **3\.  Layer 1: Infrastructure**

## **3.1  Nebari — The Open Infrastructure Standard for AI**

Nebari (https://nebari.dev) is an open-source ecosystem for deploying, managing, and scaling AI infrastructure and environments in a reproducible and governed way. Think of it the way Linux is positioned relative to computing infrastructure: Nebari is the standard layer that defines what a compliant, production-grade AI environment looks like. Nebari started as a collection of tools to enable data-science and managing learning on a cluster of machines.  It integrates with and brings together high-level applications to lower level components while helping standardize AI middleware..

Nebari standardizes:

* Compute and environment management across cloud and on-premise infrastructure

* Model deployment and versioning with reproducibility built in

* Tooling interoperability and integration patterns across the AI/ML ecosystem

* Role-based Access control, audit logging, and governance primitives

Crucially, Nebari is open-source and additive.  Most organizations will already be using some aspect of Nebari and because it is modular and defined as a collection of tools, the components of Nebari can be used a la carte and be added to any existing infrastructure choices. Its openness is not a liability — it is the strategic moat. The same dynamic that made NumPy the universal array standard (and made the rest of the scientific Python ecosystem possible) applies here: when the infrastructure layer is open, trust compounds and adoption accelerates. Travis Oliphant, the original creator of NumPy and a co-founder of Anaconda, brings exactly this institutional credibility and ecosystem-building experience to the Nebari project. Dharhas Pothina, who has been guiding Nebari's development for the past six years, brings deep experience deploying open source in the enterprise and in government to open-source projects.

## **3.2  Nebi — The Packaging and Reproducibility Layer**

Nebi is the installation foundation to Nebari that handles definition, installation, and lifecycle management of complex deployable environments. If Nebari is the operating system, Nebi is the environment manager — the mechanism by which AI environments, models, dependencies, Frames, Cogs, and Ops are specified, versioned, and deployed with full reproducibility.

Nebi's role in the architecture is foundational:

* It defines the common format by which Frames, Cogs, and Ops can be packaged for distribution

* It manages dependencies and environment snapshots so that an Op installed in one Hub behaves identically (within generative AI limits) to the same Op installed in another

* It enables versioned rollout and rollback of AI systems, contextual Frames, and the Cogs that depend on them

* It provides the installation primitive and reproducibility guardrails that makes the marketplace technically possible

Nebi is the bridge between the open-source ecosystem standard and the Frame / Cog / Op ecosystem. Without Nebi, these artifacts would be application-layer agreements without infrastructure-layer enforcement. With Nebi, reproducibility is guaranteed by construction.

## **3.3  The Intelligence Hub — The Organizational Deployment**

An Intelligence Hub is what you get when a particular configuration of Nebari is deployed inside an organizational perimeter. It is the concrete realization of the standard: a running system that integrates models, data, business systems, workflows, and the organization's accumulated Frames into a unified, governed AI control plane.

| Concept | Definition |
| :---- | :---- |
| Nebari (and all open-source AI) | The open standards and infrastructure toolkit |
| Intelligence Hub | A deployed instance of Nebari plus related open-source tools within an organization |
| Relationship | Nebari is to the Hub as Linux is to a running server |

The Intelligence Hub is the centerpiece of the overall architecture. It is where Frames are made manifest and connected to a Cog. It is where Cogs are referenced, installed, configured, and run against organizational Frames. It is where Ops orchestrate Cogs to deliver business outcomes. It is where an organization's AI capabilities live. And it is what connects an organization outward to the marketplace — both as a consumer of Frames, Cogs, and Ops published by others and, over time, as a publisher of its own.

Key characteristics of an Intelligence Hub:

* Ops inside the organization's own infrastructure perimeter (cloud, on-premise, or hybrid)

* Integrates with existing enterprise systems and applications (ERP, CRM, data warehouses, APIs)

* Enforces organizational governance policies on model behavior and data access

* Stores, versions, and manages the inheritance graph of organizational Frames

* Provides full auditability of AI actions and decisions

* Connects bidirectionally to the OpenTeams marketplace for Frame, Cog, and Op discovery and publication

# **4\.  Layer 2: Execution — Frames, Cogs, and Ops**

## **4.1  The Insight: From Models to Work**

The critical gap in enterprise AI today is not at the model layer. Foundation models are powerful and improving rapidly. The gap is at the execution layer: how do you take a capable model and turn it into a reliable, auditable, governable unit of work that a real enterprise can deploy, manage, and trust? And — equally important — how do you make sure that the organizational context that fuels the ROI of AI stays with the organization that produced and enriched it, rather than dissipating into prompt-engineering one-offs and vendor-side conversation logs?

This is the problem that Frames, Cogs, and Ops solve together. They form a layered execution model that bridges infrastructure to outcome — with context preserved at every level.

| The Progression of Value |
| :---- |
| Models   →  predict tokens |
| Frames   →  orient humans and agents to shared context, terminology, and norms |
| Cogs     →  automatically turn prompts into generative outputs oriented by Frames |
| Ops      →  deliver outcomes with human oversight orchestrating specialized Cogs |
|  |
| Each layer adds structure, purpose and enables distributed governance, autonomy, and accountability. |

## **4.2  Frames — Shared Cultural Alignment**

A Frame is a scoped, text-based artifact — a file or folder of files using an open spec — that carries the cultural and operational context within which work happens. Every organization has implicit context: brand voice, technical terminology, regulatory constraints, departmental conventions, team norms, project goals. Today, this lives in style guides, wikis, Slack history, onboarding documents, and the heads of senior employees. When AI is brought to bear without this context, the organization must re-explain itself in every interaction, and the resulting work suffers — generic, inconsistent, and disconnected from how the organization actually operates.

Frames make this context explicit, portable, inheritable, nestable, and shareable. A Frame is read by humans, applied by Cogs, and portions exchanged across organizational boundaries when appropriate. Frames are first-class artifacts: they live independently of Cogs and Ops and can be authored, discovered, exchanged, and inherited on their own.

A Frame typically carries a mix of cultural context (the why and what of the work) and the concrete artifacts that operationalize that context (the how and with what):

* Rules — what is and is not acceptable behavior within the scope

* Terminology — the words, names, and definitions specific to the organization, function, or project

* Goals — what success looks like; what outcomes are valued

* Style — tone of voice, formatting conventions, brand expression

* Norms — implicit expectations about how work gets done

* Skills — named capabilities the work depends on

* Tool specifications — Nebi spec files that document the tools the Frame expects to be available

* Prompts — reusable prompt fragments to be loaded into Cog context

* Architecture descriptions — relevant software and system context that orients the work

* Business process details — the procedural backbone that the work follows

Frames are characterized by five essential properties:

| Property | What It Means | Why It Matters |
| :---- | :---- | :---- |
| Scoped | Each Frame applies to a defined scope: organization, department, team, project, role, or relationship | Context applies where it should, and not where it shouldn't |
| Inheritable | A child Frame inherits and extends a parent Frame (project inherits department inherits company) | Organizational hierarchy is reflected in context propagation; the chain of authority is auditable |
| Composable | Multiple Frames can be combined for a given work session | A user can layer company \+ department \+ project \+ ad-hoc context as the work requires |
| Shareable | Frames can be shared internally with colleagues or selectively externally with partners, vendors, and customers | Context flows where collaboration requires; reviewed subsets protect what should remain internal |
| Discoverable | Frames can be published to internal libraries, communities of practice, and open registries where others find and adopt them | Context portability extends beyond direct relationships; the vast majority of Frames spread through community adoption rather than commercial sale |

### **Why Frames Are a Distinct Architectural Layer**

It would be tempting to think of Frames as just "prompts" or "system messages" — context that an AI provider could supply through their API. This understates what Frames are. A Frame is not a prompt; it is an organizational artifact governed by the organization that owns it. Frames are versioned, audited, owned, inherited, and exchanged. They embody competitive intelligence, regulatory knowledge, brand identity, and operational doctrine. They are the cultural commons of the organization, made explicit and portable, but also protectable and governed and something worth preserving within a private cognitive context and not just shared with a rented intelligence.

Concretely, an organization might maintain Frames such as:

* A Brand Voice Frame published by the marketing function, used by every Cog that drafts external communications

* A Healthcare Compliance Frame maintained by the legal team, applied to any Cog touching patient data

* A Q4 Sales Playbook Frame shared across the sales organization for the duration of the quarter

* An External Vendor Frame, with selectively-shared sections, given to a procurement partner so their AI work aligns with the organization's expectations

* A Pharma R\&D Compliance Frame published by an industry consortium and adopted by hundreds of pharmaceutical companies for use in their Hubs

### **Frames in Practice: Five Example Use Cases**

Beyond the architectural definition, Frames can address specific human alignment problems that every organization faces — and that AI traditionally makes worse, not better. OpenTeams itself uses Frames across these dimensions, and we expect every organization adopting an Intelligence Hub will find similar opportunities to use Frames to facilitate collaborative efficiency: 

**1\.  Internal alignment across the company.** Every organization accumulates implicit context such as vocabulary, values, brand voice, and operating norm. This implicit context grows faster than any onboarding program can capture. Today that context lives in style guides, wikis, Slack archives, and the heads of senior employees, where new hires cannot easily reach it and AI systems cannot effectively be oriented by it. OpenTeams maintains a Company Frame that codifies its vocabulary, brand voice, strategic narrative, and core values. Every division, team, project, and individual Frame inherits from it. Every Cog conversation an OpenTeams employee has, and every Op an OpenTeams employee launches, is oriented by it. Brand and policy alignment compounds with use. 

**2\.  Aligning sister companies and ecosystem peers.** OpenTeams operates within an ecosystem of related organizations that share strategic direction without sharing corporate boundaries. By publishing Product Direction Frames, OpenTeams gives these sister organizations' teams and AI workers access to the latest product thinking, roadmap, vocabulary, and positioning. The alignment travels through the relationship; the corporate boundaries remain intact. What used to require quarterly all-hands and an inevitable lag in shared understanding becomes a single artifact that everyone inherits and updates in place.

**3\.  Keeping open-source communities aligned.** Open-source communities depend on alignment — shared vocabulary, contribution conventions, technical standards, project governance. By publishing Community Frames, project maintainers give every contributor (and every AI worker assisting a contributor) the context needed to participate without first reading every wiki page and Slack archive. Nebari, the broader Python AI ecosystem, and adjacent communities stand to benefit substantially from this mode of coordination — and OpenTeams will lead by publishing Community Frames for the projects we steward.

**4\.  The foundation of partner engagement.** Every external relationship at OpenTeams — system integrators, technology partners, channel resellers, customer engagements — can begin with a Partner Frame. The partner installs the Frame; their teams and their AI workers immediately operate in OpenTeams' vocabulary, against OpenTeams' definitions of success, with OpenTeams' brand voice when appropriate. Partner engagement becomes architecturally repeatable instead of reinvented relationship by relationship. The Frame is the contract of context.

**5\.  How we message to investors.** Investor communication is the highest-leverage messaging an organization produces. OpenTeams maintains an Investor Frame that codifies the strategic narrative, the financial vocabulary, the proof points, and the voice for investor audiences. Pitch decks, briefings, follow-up conversations, and investor-facing AI work all inherit from it. The risk of message drift at scale — where different team members tell subtly different versions of the company's story — becomes structurally unlikely. The Investor Frame keeps the narrative coherent across every surface where it appears.

These five use cases share a pattern. Each begins with a coordination problem that scales painfully — internally, across ecosystems, externally. Each is currently addressed (when at all) through ad-hoc documents, repeated meetings, and the slow propagation of tribal knowledge. Each is solved cleanly by a Frame: a single, versioned, inherited, shareable artifact that carries the right context wherever it needs to go. This is what we mean when we say Frames are infrastructure for organizational alignment.

The Frame spec — an open specification for how these artifacts are structured — is the standard that makes this exchange possible. Just as Nebari standardizes infrastructure and Nebi standardizes packaging, the Frame spec and concept standardizes cultural alignment. Together they form the open foundation on which the entire distributed AI economy is built.

## **4.3  Cogs — AI Workers Oriented by Frames**

A Cog is a discrete, AI-powered worker. It is the atomic unit of AI work within the system. A Cog encapsulates:

* A model that may be tailored or specialized for a set of tasks (e.g., document classification, data extraction, code review, customer response generation, accounting recommendations, marketing acumen)

* A context, defined by one or more Frames, that orients the model to a particular kind of work within the right organizational culture

* The tools and APIs it has access to

* Its governance parameters: what data it may access, what actions it may take, what requires human approval

Cogs are important because they are the level at which AI behavior becomes auditable and governable, much like a worker. Rather than asking "what did the model do?", an organization can ask "what did this Cog do, with what inputs, under which Frames, and what was the outcome?" This specificity — combined with the Frames that orient the Cog — is what makes Cogs deployable in regulated industries and high-stakes workflows.

Cogs are not generally intended to be standalone agents, though they can be in simple circumstances. They can be interacted with directly for debugging, validation, analysis, maintenance, or simple operations. Normally, they operate within the context of an Op, which provides the coordination logic, the workflow structure, the goal-oriented looping, the validation functions, and the human oversight framework. A Cog produces an output from a model (or a collection of other Cogs); an Op combines this with other layers of the compute ecosystem in a human-led process that does the right thing with the outputs of Cogs — all of it shaped by the Frames that apply.

## **4.4  Ops — Orchestrated AI Workflows**

An Op is the application of the distributed AI economy. It is the orchestrated, supervised AI workflow that a human at the keyboard usually invokes or launches.  This is the automation at the highest level that maps onto how knowledge workers think about doing their job. "Close the books." "Onboard this customer." "Qualify this lead." "Draft this campaign." Each of those is an Op.

An Op is composed of:

* One or more Cogs — the AI workers performing discrete cognitive tasks, each carrying their own embedded Frames

* Additional Frames applied at the workflow level — context that orients the Op as a whole, beyond what individual Cogs already carry

* A supervising model that may coordinate Cog execution, sequences and parallelizes work, and handles unexpected conditions

* Human-in-the-loop feedback points where reviewers approve, refine, or redirect the AI work at meaningful checkpoints

* Integration logic for connecting to enterprise systems, data lakes, and APIs

* A Nebi-compatible manifest that specifies dependencies, environment requirements, and configuration parameters

Ops are designed to be invoked through any interface the user already finds natural:

* As an application icon clicked from the Desktop or Web-based Application launcher

* As a command typed into a CLI or chat interface

* As a button pressed or a link followed within the Intelligence Hub or other integrated business application

* As a scheduled job triggered by time, event, or external system

The Op abstraction is what makes the marketplace possible at the outcome layer. Because an Op is self-contained, versioned, and installable via Nebi, it can be authored once and deployed into any Intelligence Hub that implements the standards needed — automatically picking up the local Frames that apply. This is analogous to how an NPM or pip package is authored once and installed across millions of environments, but for supervised, Frame-aware AI workflows rather than software libraries — and adapted at install time to the consuming organization's culture and norms through Frames.

| Characteristic | What It Means | Why It Matters |
| :---- | :---- | :---- |
| Versioned | Every Op has a version identifier and changelog | Reproducibility; safe rollout and rollback |
| Installable | Deployed via Nebi into any compliant Hub or Desktop Application | Marketplace distribution at scale |
| Frame-oriented | Declares the Frames it requires or applies, and inherits those embedded in its Cogs | Same Op adapts to many organizations' contexts |
| Supervised | A coordinating model orchestrates Cog execution; humans approve and refine at defined checkpoints | Sophisticated workflows remain governable and auditable |
| Triggerable | Invoked as an icon, command, button, or scheduled job | Fits every human and automated invocation context |
| Self-contained | Includes all Cogs, supervising logic, integration specs, and Frame declarations | No environment-specific dependencies |
| Composable | Ops can invoke other Ops as sub-routines | Complex workflows from simple building blocks |

## **4.5  How Frames, Cogs, and Ops relate to "Agents"**

The term "AI agent" is increasingly overloaded and carries significant risk connotations. Typical capabilities traditionally called agents are a combination of two or more the elements explored here.  Frames, Cogs, and Ops provide agentic capability with better defined terms that can be deployed in billions of compound AI systems across the world. Frames, Cogs, and Ops deliver the automation power of AI agents with the governance guarantees real organizations require.  Their use signals that the organization is relying on the OpenTeams brand promise of ensuring that the organizational context that fuels the value of AI stays governed and managed by the organization that produced it.

# **5\.  Layer 3: The Marketplace — A Distributed Economy**

## **5.1  Three Classes of Exchanged Artifact**

The marketplace is built around three classes of exchanged artifact, each with its own dynamics:

* Ops — orchestrated, supervised AI workflows that deliver outcomes with defined accountability.  Typically these will be collected into service as software subject to subscription, usage, or outcome-based commercial arrangements.

* Cogs — AI workers that can be specialized to specific subject areas of work and therefore be deployed more easily at scale to the tasks at hand.  These can be rented, purchased, given away, or provided under usage or subscription arrangements.

* Frames — scoped artifacts that carry organizational context. The vast majority of Frames will be shared freely within the organization and between the organizations that need them. A smaller number might be offered commercially as expertise to deploy under a licensed arrangement. 

This is a key architectural decision of the OpenTeams vision. Rather than building the ecosystem and marketplace around a single class of artifact — say, just Ops, or just models — OpenTeams builds the marketplace around the three classes that actually constitute an AI economy: the work, the workers, and the context that orients them. Each class has its own publishers, its own audience, and its own dynamics.

The Frame side of the economy is primarily about coordination and shared abstraction, not transaction. Communities of practice publish Frames so members can align on terminology and methods. Industry consortia publish Frames that encode best practices. Open-source ecosystems publish Frames that make it easy to adopt their tools and conventions. Within organizations, departments and teams publish Frames so that work flows consistently across people, partners, and AI systems. The marketplace is where this sharing happens at scale — most of it free, some of it commercial, all of it organized around the open Frame spec.

## **5.2  The Network Flywheel**

The Intelligence Hub and Frame / Cog / Op architecture creates a compounding platform flywheel:

| The Growth Engine |
| :---- |
| 1\.  More Intelligence Hubs deployed  →  larger addressable market for Frame, Cog, and Op publishers |
| 2\.  More Frames, Cogs, and Ops available  →  greater value proposition for new Hub deployments |
| 3\.  More Hub deployments  →  more data on what works  →  better artifact quality across the ecosystem |
| 4\.  Better artifacts  →  stronger marketplace  →  more Hub deployments |
|  |
| Each cycle deepens the moat. The flywheel is self-reinforcing. |

This is the economic architecture that differentiates OpenTeams from pure infrastructure providers (who capture only deployment value) and from pure marketplace platforms (who have no infrastructure moat). The combination of Nebari, Nebi, and other open-source standards as trusted foundations, Frames as a portable container for organizational context, and Ops and Cogs as governed units of exchange creates a platform that is difficult to replicate and more valuable with every participant that engages.

## **5.3  Who Participates**

| Participant | Role in the Ecosystem | Value Received |
| :---- | :---- | :---- |
| Enterprises | Deploy Intelligence Hubs; author Frames; install Ops, Cogs, and external Frames | Owned AI capabilities; preserved organizational context; compliance; reduced integration cost |
| AI Developers | Build and publish Ops and Cogs | Revenue; distribution; market access |
| Domain Experts | Author Frames that capture expertise; configure Cogs; define workflow logic for Ops | Influence and recognition through widely-adopted Frames; community contribution; optional commercial offerings |
| Communities & Consortia | Publish open Frames that codify shared methodologies, vocabularies, and standards for their domain | Member alignment; ecosystem cohesion; influence on industry direction |
| Consultancies & Agencies | Publish methodology Frames — most as open community contributions, some as commercial offerings | Brand recognition; client adoption of shared methods; optional revenue from commercial Frames |
| System Integrators | Deploy and customize Hubs; build bespoke Ops and Frames | Services revenue; recurring relationships |
| Open-Source Contributors | Extend Nebari, Nebi, and the Frame spec as well as Cog and Op standards stored in Nebari. | Reputation; ecosystem participation; influence over the standard |

# **6\.  The Gateway: The Intelligence Hub Desktop Application**

## **6.1  Why a Desktop Application Is Not Optional**

The three-layer architecture described above is technically coherent and economically sound. But architecture alone does not create adoption. The critical product that makes the Intelligence Hub tangible, accessible, and compelling to the people who must use it every day is a Desktop Application (with web access where appropriate).

This is not a "nice-to-have" product enhancement. The Desktop Application is the primary interface through which the entire system becomes real for end users. Without it, Intelligence Hubs are server-side configurations that require engineering expertise to operate. With it, any knowledge worker in an organization can combine the Frames that orient their work, converse with AI Cogs that already understand their context, run pre-configured Ops to automate their processes, and share organizational context with internal teammates and external partners.

## **6.2  The Target User: Knowledge Workers**

The Desktop Application is designed for the people who do the daily operational work of modern organizations — sales, marketing, project success, accounting, legal, HR, IT, and the other back-office and shared-service functions that keep enterprises running. These users:

* Operate inside well-defined organizational contexts — their function, their team, their accounts, their projects

* Apply organizational norms, terminology, and policies to every task they touch

* Need AI augmentation that respects those contexts — not generic AI that has to be re-oriented at the start of every interaction

* Routinely share context across organizational boundaries — with partners, vendors, customers, and external collaborators

* Are not engineers and cannot be expected to configure, manage, update, or operate Hubs, Ops, or Cogs at the configuration layer

For these users, the Desktop Application provides a unified surface where Frames, Cogs, and Ops come together to enable specialized work — without requiring the user to understand the architecture beneath them.

## **6.3  Local Memory: Absorbing Shared Context**

At the heart of the Desktop Application is a personal local memory that absorbs the user's active Frames. When a user joins an organization, they inherit the Company Frame. When they join a department, the Department Frame layers on top. When they join a project, the Project Frame composes further. The user can install additional Frames from the marketplace (a regulatory Frame for their industry, a brand voice Frame from a partner agency), and they can author personal Frames for the way they themselves prefer to work.

This combination — the user's personal, inherited, installed, and authored Frames — is held in the Desktop Application's local memory and becomes the contextual substrate that orients every AI interaction. A conversation with a Cog automatically inherits this context. An Op launched from the application runs against this context. The user does not need to re-explain who they are, who their company is, or how their team works. The context is already there.

Local memory is private to the user by default. Frames can be promoted from local memory back to the Hub, shared with teammates, or selectively shared with external partners — but the user controls the boundary.

## **6.4  The Three Modes of AI Engagement**

Through the Desktop Application, users engage with AI in three complementary modes:

### **Mode 1 — Applications (Ops)**

A dedicated tab presents pre-configured Ops as visual icons, like an application launcher. Users click an Op icon to run an automated process: generate a quarterly board report, draft a customer onboarding plan, reconcile expense reports, run a quarterly compliance review. Ops are the "buttons that do the job" — discrete, repeatable units of organizational work, each optionally picking up the user's active Frames or configured to only use the pre-loaded Frames.

### **Mode 2 — Conversations (Cogs)**

A chat surface where users have natural-language conversations with Cogs that have been oriented by their currently-active Frames. This is the iterative workspace: ask a question, get domain-aware help, draft a document, debug a problem, brainstorm an approach. Because the Cog inherits the user's combined Frame context, the conversation already knows the company's brand voice, the department's terminology, the project's goals, the appropriate tools that ensure the outputs are preserved.  This is done without the user having to set the stage.

### **Mode 3 — Cog Library**

Users can also load specific Cogs directly for specialized tasks — running a Cog as a standalone tool when they need its specific capability without the conversational layer. This is useful for analysis, validation, debugging, one-off specialized work, and exploring what Cogs exist in the Hub or the marketplace.

## **6.5  Frame Management: Composition and Sharing**

The Desktop Application's most distinctive capability is Frame management. Users can:

* Install Frames from the marketplace, their organization's internal Frame library, or external partners who have shared them

* Combine multiple Frames for a given work session, such as company \+ department \+ project \+ ad-hoc context layered together, with the application managing the inheritance graph

* Author new Frames or extend existing ones, capturing the context they want to make repeatable

* Share Frames internally with colleagues, or externally with partners, vendors, and customers using selective field-level controls so internal-only sections stay internal

* Provide feedback on Frames in the form of both scores on particular concepts in the Frame with a 6 point scale (-10, \-1, \-0, \+0, \+1, \+10) or via suggested changes to the Frame that are sent back to the accountable author for review.

* Publish Frames back to the organization's library, a community board, a particular user, the open marketplace, or both

This makes the Desktop Application both a  productivity surface and a context exchange.  It is the place where organizational alignment is made portable. A sales representative can share a Sales Methodology Frame with a partner to align them on terminology and stages. A marketing director can publish a Brand Voice Frame to every external agency that the company works with. A legal team can issue a Vendor Compliance Frame that every supplier's AI tooling automatically respects.

## **6.6  Intelligence Hub Health and Governance**

For users with administrative privileges, the Desktop Application is also the operational dashboard for the Intelligence Hub itself:

* Real-time view of Hub resource utilization and model serving status

* Audit log browser: full history of AI actions, human interventions, Frame applications, and data accesses

* Policy management: define and update governance rules that apply across all Frames, Ops, and Cogs

* User and role management: control who can install Frames, configure Cogs, run Ops, and review outputs

## **6.7  The Desktop Application as a Market Development Tool**

Beyond its operational value, the Desktop Application plays a crucial strategic role in market development. The adoption of a new infrastructure standard — whether Linux, Python, or Kubernetes — always depends on a compelling end-user experience. The Desktop Application is that experience for the Intelligence Hub ecosystem.

* Lowers the barrier to Hub deployment by making configuration visual and guided rather than requiring deep engineering expertise

* Accelerates Frame, Cog, and Op adoption by making discovery intuitive — users browse the marketplace the way they browse an app store

* Creates a feedback loop: usage data from the Desktop Application informs Frame and Op quality rankings, surfaces unmet needs, and guides developer investment

* Enables the Applied AI Society and credentialing programs to use the Desktop Application as a hands-on training environment

* Demonstrates the platform's value proposition in enterprise sales contexts — nothing closes a deal faster than a working demo of a knowledge worker doing their job, with AI, under the right Frames

## **6.8  Technical Architecture**

The Desktop Application is built as a cross-platform native application (macOS, Windows, Linux), with web access where appropriate, connecting to the user's Intelligence Hub via local or network API. Key architectural characteristics:

* Local-first: the application can operate with full functionality against a local Hub even when a remote Hub and/or marketplace is not reachable

* Hub-agnostic: the same application works against any Nebari-compliant Intelligence Hub, regardless of where it is deployed

* Nebi-integrated: Frame, Cog, and Op installation and lifecycle management are handled natively through the Nebi client

* Marketplace-connected: browsing and discovery connect to the OpenTeams marketplace API when network access is available

* Local-memory-backed: the user's combined Frame context is held locally for privacy, performance, and offline operation

* Extensible: a plugin architecture allows Op developers to provide custom configuration UIs for their Cogs, surfaced natively within the Desktop Application

# **7\.  The Role of Nebari and Nebi in the Broader Ecosystem**

## **7.1  Nebari as the Trust Foundation**

The Intelligence Hub marketplace only works if participants trust that an Op installed in one Hub will behave the same way in another, that a Frame inherited by one Cog will be interpreted the same way by another, and that the specs on which all of this depends are stable and open. That trust is grounded in Nebari. Because Nebari is open-source, its specification is publicly auditable including the definitions and patterns exposed as Frame, Cogs, and Ops.  While Nebari is initially company backed so that it can be nurtured and improved with a focused approach, it is desired that it become a community-governed standard so that multiple stakeholders can contribute to its development. This is the same dynamic that made Python the universal language for AI.  The openness amplifies the trust that proprietary alternatives can struggle to provide..

Nebari's open-source nature also creates an important flywheel for the marketplace itself. As more organizations deploy Intelligence Hubs using components of Nebari, the standard becomes more deeply entrenched. Frame, Cog, and Op publishers gain access to every Hub in the network. The standard's adoption is self-reinforcing, and OpenTeams — as the primary steward and commercial entity behind Nebari — captures some of the value of those network effect through enterprise services, marketplace fees, and direct ecosystem participation with our own Cogs and Ops.

## **7.2  Nebi as the Distribution Mechanism**

Nebi is what turns the marketplace from a concept into a mechanism. It answers the question: "How does a Frame, Cog, or Op actually get distributed?” The answer is Nebi, and environment management tool that handles the full lifecycle from specification to deployment to update to removal.

Nebi's importance in the OpenTeams economy is analogous to pip's importance in the Python ecosystem or npm's importance in the JavaScript ecosystem. It is the distribution plumbing that developers, organizations, and end users can rely on, freeing them to focus on authoring and using Frames, Cogs, and Ops rather than on the mechanics of deployment.

Nebi also plays a trust role. When a Frame, Cog, or Op is installed via Nebi, the environment ensures that all dependencies are resolved and pinned, and the installation is logged. Every deployment is fully auditable — an important guarantee for regulated industries.

## **7.3  The Startup Ecosystem**

One of the most significant long-term opportunities in this architecture is the startup ecosystem that the Intelligence Hub movement engenders.  Just as Kubernetes created a generation of cloud-native startups that built on top of the container orchestration standard, Nebari and Nebi create the foundation for a generation of deeply specialized, domain-expert-filled AI businesses that use Intelligence Hubs, publish vertical Ops and Cogs, and — uniquely — publish Frames that monetize accumulated organizational and industry knowledge.

A domain expert in healthcare informatics can deploy their specific Nebari Hub, build Ops and Cogs specialized to clinical workflows, and publish a HIPAA Compliance Frame that any healthcare organization can adopt. Most of these Frames will be shared openly to align an industry around best practices; a smaller number may be offered commercially. A consultancy can publish its methodology as a Frame — earning influence and brand recognition through adoption, with optional commercial variants. A law firm can publish a Contract Review Frame that codifies its expertise in a form clients and partners can adopt. The same pattern applies across energy, agriculture, legal, financial services, government, and beyond.

This vertical specialization — enabled by the open standard and the three-class marketplace — is what ultimately drives the platform to scale. OpenTeams does not need to build every vertical Frame, Cog, or Op. It needs to build the infrastructure and marketplace that makes it economically attractive for domain experts to build them themselves.

# **8\.  Competitive Positioning**

The combination of Nebari, Intelligence Hubs, Frames, Cogs, Ops, and the Desktop Application creates a competitive position that is difficult to replicate from any single direction:

| Competitor Type | What They Offer | What They Lack |
| :---- | :---- | :---- |
| Foundation Model Providers (OpenAI, Anthropic, Google) | Powerful models via API | Infrastructure standard; execution layer; portable context (Frames); marketplace; sovereignty |
| Cloud AI Platforms (AWS SageMaker, Azure ML) | Managed model deployment | Open standard; Frame-based context portability; Op/Cog ecosystem; marketplace; desktop experience |
| Agent Frameworks (LangChain, AutoGen) | Agent orchestration libraries | Infrastructure; governance; installable packages; enterprise trust; context-sharing spec |
| Enterprise Software Vendors (Salesforce, ServiceNow) | Vertical AI features | Open standard; extensibility; cross-domain Frame/Op marketplace; sovereign deployment |
| OpenTeams \+ Nebari | All three layers: infra \+ execution (with Frames, Cogs, Ops) \+ economy | — |

The most defensible moat in this architecture is the compounding of three reinforcing layers: open-source trust (Nebari and Nebi), portable organizational context (Frames), and marketplace network effects (the three-class economy). Each reinforces the others. Trust drives Hub adoption. Hub adoption drives Frame, Cog, and Op publication. The Frame catalog locks in cultural alignment that is hard to replicate elsewhere. The combined catalog drives marketplace value. Marketplace value drives more Hub deployments. This is a flywheel that compounds over time and becomes increasingly difficult to displace.

# **9\.  Strategic Roadmap**

| Phase | Focus | Key Milestones |
| :---- | :---- | :---- |
| Phase 1(Now – 6 months) | Infrastructure \+ Execution foundation | Nebari Hub deployment hardened; Nebi packaging standard defined; Frame spec v1 published; first Ops, Cogs, and Frames built; Desktop Application alpha released |
| Phase 2(6 – 18 months) | Marketplace emergence | Public marketplace live for Frames, Cogs, and Ops; 50+ Ops and 100+ Frames available; Desktop Application general availability; first vertical ecosystems (health, energy, legal) |
| Phase 3(18 – 36 months) | Network effects \+ ecosystem | 1,000+ deployed Hubs; 500+ Ops and 2,000+ Frames; consultancies, communities of practice, and domain experts actively publishing Frames for shared alignment; Applied AI Society credentialing; international Hub networks |

# **10\.  Conclusion: The Infrastructure for the Intelligence Economy**

The Intelligence Economy is not a metaphor. It is the inevitable next stage of enterprise computing: a world in which AI capabilities are owned, deployed, exchanged, and governed as core operational infrastructure — and in which the organizational context that makes AI valuable is itself a first-class artifact that can be authored, inherited, shared, and exchanged.

OpenTeams, built with and for open source, is building the infrastructure for this economy. Nebari forms a foundation of open-source capability that is deployed into private infrastructure that is owned by the organization.  The Intelligence Hub is the organizational locus of owned and accountable AI. Frames are the portable containers and specifications for the rules, terminology, goals, style, and norms that make AI work specialized rather than generic. Cogs are the governed AI workers that operate within those Frames. Ops are the installable, exchangeable units of AI-driven work that combine Cogs and Frames into business outcomes. Nebi is the distribution mechanism that makes all of these technically possible to exchange. And the Desktop Application is the product that makes everything accessible to everyday knowledge workers who must ultimately use and trust it — sales, marketing, project success, accounting, legal, HR, IT, and the rest of the operational backbone of every modern organization are the first customers.

This is not a vision built on hope. It is built on the same pattern that Travis Oliphant and his team have executed before: create the open standard, drive adoption through trust and ecosystem participation, and capture the commercial value of the network that forms around it. NumPy standardized arrays. Anaconda distributed the Python data science stack. Nebari is standardizing AI infrastructure — and the Frame, Cog, and Op marketplace is the economy that forms on top of it.

| The Opportunity in One Sentence |
| :---- |
| OpenTeams is building the Linux \+ App Store for scalable enterprise AI — |
| where Intelligence Hubs are the servers, Nebari is the open source ecosystem that enables integration with the underlying OS, Nebi is the modular reproducibility specification. |
| Frames carry the shared culture and context, Cogs are the AI workers, |
| Ops are the orchestrated applications they execute together, |
| and the Desktop Application is the interface that makes it all real to the human at work. |

OpenTeams  |  nebari.dev  |  Confidential — April 2026  |  Revision 4
