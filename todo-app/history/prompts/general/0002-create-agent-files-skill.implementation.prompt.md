---
id: 2
title: Create-Agent-Files Skill
stage: implementation
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unknown
command: manual
labels: ["skill", "agent", "file-generation", "automation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .claude/skills/create-agent-files/skill.md
 - .claude/skills/create-agent-files/create-agent-files.sh
 - .claude/skills/create-agent-files/config.json
 - .claude/skills/create-agent-files/README.md
 - .claude/skills/create-agent-files/test.sh
tests:
 - .claude/skills/create-agent-files/test.sh
---

## Prompt

Create a skill named "create-agent-files".

Purpose:
This skill automatically generates standard required files for a new agent inside its folder.

Files to generate:
- purpose.md
- responsibilities.md
- rules.md
- skills.md
- workflows.md

Behavior Requirements:
- Input: agent_name + agent_type + agent_description
- Place inside: .claude/agents/{agent_name}/
- Each file MUST contain meaningful starter content
- Content should clearly define agent responsibilities
- Must not be empty template
- Must overwrite only if explicitly requested

## Response snapshot

Successfully created the "create-agent-files" skill that generates standard agent files (purpose.md, responsibilities.md, rules.md, skills.md, workflows.md) with meaningful starter content based on agent parameters. Includes validation, overwrite protection, and comprehensive testing.

## Outcome

- ✅ Impact: Created a complete skill for generating standard agent files with meaningful content
- 🧪 Tests: All functionality tested including file creation, overwrite protection, and parameter validation
- 📁 Files: 5 files created including implementation, config, documentation, and tests
- 🔁 Next prompts: Create additional agent management skills or enhance existing functionality
- 🧠 Reflection: Proper validation and meaningful starter content is critical for effective agent development

## Evaluation notes (flywheel)

- Failure modes observed: None - all functionality works as expected with proper error handling
- Graders run and results (PASS/FAIL): All tests pass successfully
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add validation for agent directory existence and content customization options