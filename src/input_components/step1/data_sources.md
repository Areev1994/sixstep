USER-PROVIDED INPUTS (Check FIRST):
- active/{problem_id}/input_dump/ - User-provided materials (logs, specs, screenshots, config files, etc.)
- Check this directory FIRST for problem-specific context before searching project memory or codebase
- If empty, proceed to project memory sources below

---

PRIMARY KNOWLEDGE SOURCES:

**Project Memory Structure**:
- Built incrementally through six-step sessions (may be incomplete)
- Three layers: Architecture, Features, Solutions
- `system_overview.md` shows high-level component relationships (text/ASCII diagrams)
- Each `architecture/component/README.md` includes internal component structure diagram
- Architecture explains component **ROLES**, not implementation details
- Directory structure is flexible, doesn't mirror every source directory

---

**1. Project Memory** (Primary source):

**Architecture Layer** (Component understanding):
- `project_memory/architecture/system_overview.md` - System-wide component relationships diagram
- `project_memory/architecture/[component]/README.md` - Component-specific roles, internal diagrams, source locations, interfaces

**Features Layer** (Capability overviews):
- `project_memory/features/[feature]/README.md` - What feature is, why it exists, when to use

**Solutions Layer** (Past patterns - light reference only):
- `project_memory/solutions/*.md` - Quick reference to see if similar problems exist

**2. Codebase Search** (Secondary - only when project memory lacks information):
- Source code and headers
- Documentation and README files
- Configuration and build files

---

**EXAMPLE** (showing where to find information):

Problem: "Optimize slow API response times"

**Data sources to check:**

1. **User-provided inputs (check first):**
   - `input_dump/` - Check for performance logs, error traces, configuration files

2. **Project Memory (primary):**
   - `project_memory/architecture/system_overview.md` - Shows API architecture components
   - `project_memory/features/caching/README.md` - Describes caching capabilities
   - `project_memory/solutions/api_optimization_*.md` - Past API optimization solutions

3. **Codebase (if needed):**
   - API gateway configuration files
   - Service layer implementation
   - Database connection settings

**Result:** Information about API architecture and caching found in project memory. Can build diagram and identify factual context questions.

Note: This is Step 1, so no previous guide files exist yet.