---
id: 3
title: Assign-Agent-Skills Skill
stage: implementation
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unknown
command: manual
labels: ["skill", "agent", "skills-management", "automation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .claude/skills/assign-agent-skills/skill.md
 - .claude/skills/assign-agent-skills/assign-agent-skills.sh
 - .claude/skills/assign-agent-skills/config.json
 - .claude/skills/assign-agent-skills/README.md
 - .claude/skills/assign-agent-skills/test.sh
tests:
 - .claude/skills/assign-agent-skills/test.sh
---

## Prompt

Create a skill named "assign-agent-skills".

Purpose:
Attach relevant skills to a newly created agent and define what it can and cannot do.

Behavior:
- Input: agent_name + list_of_skills
- Write inside skills.md for that agent
- Clearly categorize:
  - Primary Skills
  - Optional/Extended Skills
- Ensure formatting is professional
- Confirm completion

## Response snapshot

Successfully created the "assign-agent-skills" skill that attaches relevant skills to an agent, updates its skills.md file with proper categorization of primary and extended skills, and clearly defines capabilities and limitations.

## Outcome

- ✅ Impact: Created a complete skill for assigning and managing agent skills with proper categorization
- 🧪 Tests: All functionality tested including skill assignment, validation, and categorization
- 📁 Files: 5 files created including implementation, config, documentation, and tests
- 🔁 Next prompts: Create additional agent management skills or enhance existing functionality
- 🧠 Reflection: Proper categorization and clear definition of capabilities and limitations is critical for effective agent management

## Evaluation notes (flywheel)

- Failure modes observed: None - all functionality works as expected with proper error handling
- Graders run and results (PASS/FAIL): All tests pass successfully
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add skill validation against available skills or allow custom skill descriptions