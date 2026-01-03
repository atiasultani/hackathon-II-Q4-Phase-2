---
id: 5
title: Create-Sub-Agent Skill
stage: implementation
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unknown
command: manual
labels: ["skill", "agent", "sub-agent", "hierarchy", "automation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .claude/skills/create-sub-agent/skill.md
 - .claude/skills/create-sub-agent/create-sub-agent.sh
 - .claude/skills/create-sub-agent/config.json
 - .claude/skills/create-sub-agent/README.md
 - .claude/skills/create-sub-agent/test.sh
tests:
 - .claude/skills/create-sub-agent/test.sh
---

## Prompt

Create a skill named "create-sub-agent".

Purpose:
Create a dependent sub-agent under a parent agent.

Behavior Requirements:
- Input: parent_agent + sub_agent_name + purpose
- Create folder: .claude/agents/{parent}/{sub-agent}
- Generate:
  - purpose.md
  - responsibilities.md
  - skills.md
- Link sub-agent to parent intelligently
- Register it as a hierarchical agent

## Response snapshot

Successfully created the "create-sub-agent" skill that creates hierarchical sub-agents under parent agents with proper folder structure, documentation, and parent-child linking.

## Outcome

- ✅ Impact: Created a complete skill for creating hierarchical sub-agents with proper parent-child relationships
- 🧪 Tests: All functionality tested including sub-agent creation, duplicate prevention, and parent linking
- 📁 Files: 5 files created including implementation, config, documentation, and tests
- 🔁 Next prompts: Create additional agent hierarchy management skills or enhance existing functionality
- 🧠 Reflection: Proper hierarchical structure with parent-child linking is critical for complex agent systems

## Evaluation notes (flywheel)

- Failure modes observed: None - all functionality works as expected with proper error handling
- Graders run and results (PASS/FAIL): All tests pass successfully
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add sub-agent dependency tracking or hierarchical registry management