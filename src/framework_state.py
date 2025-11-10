#!/usr/bin/env python3
"""
Six-Step Framework State Management
Handles detection-logic and state transitions as per solution map
"""

import json
import sys
from pathlib import Path
from datetime import datetime

class FrameworkState:
    def __init__(self):
        # Use absolute paths based on the script location
        script_dir = Path(__file__).parent
        self.state_file = script_dir / "current_state.json"
        self.active_dir = script_dir / "active"
        self.meta_dir = script_dir / "meta"
        self.completed_dir = script_dir / "completed"
        self.components_dir = script_dir / "input_components"
        self.framework_info_file = self.components_dir / "framework_info.md"
        
        # Validate required directory structure exists
        self._validate_paths()
        
        # Step and phase definitions
        self.steps = {
            "1": {"name": "Understanding Problem Statement", "phases": [1]},
            "2": {"name": "Current Situation Assessment", "phases": [1]}, 
            "3": {"name": "Brainstorming Session", "phases": [1, 2]},  # Phase 1: brainstorm, Phase 2: task list
            "4": {"name": "Implementation", "phases": [1]},
            "5": {"name": "Testing & Optimization", "phases": [1]},
            "6": {"name": "Insights Extraction", "phases": [1]}
        }
        
        # Input component file paths per step/phase (as per solution map)
        self.input_component_files = {
            ("1", 1): {
                "step_info": "step1/step_info.md",
                "data_sources": "step1/data_sources.md",
                "output_requirements": "step1/output_requirements.md"
            },
            ("2", 1): {
                "step_info": "step2/step_info.md",
                "data_sources": "step2/data_sources.md",
                "output_requirements": "step2/output_requirements.md"
            },
            ("3", 1): {
                "step_info": "step3/phase1_step_info.md",
                "data_sources": "step3/phase1_data_sources.md",
                "output_requirements": "step3/phase1_output_requirements.md"
            },
            ("3", 2): {
                "step_info": "step3/phase2_step_info.md",
                "data_sources": "step3/phase2_data_sources.md",
                "output_requirements": "step3/phase2_output_requirements.md"
            },
            ("4", 1): {
                "step_info": "step4/step_info.md",
                "data_sources": "step4/data_sources.md", 
                "output_requirements": "step4/output_requirements.md"
            },
            ("5", 1): {
                "step_info": "step5/step_info.md",
                "data_sources": "step5/data_sources.md",
                "output_requirements": "step5/output_requirements.md"
            },
            ("6", 1): {
                "step_info": "step6/step_info.md",
                "data_sources": "step6/data_sources.md",
                "output_requirements": "step6/output_requirements.md"
            },
            # Special entry for step-done preference extraction
            ("step-done", 1): {
                "framework_info": "step-done/framework_info.md",
                "step_info": "step-done/step_info.md",
                "data_sources": "step-done/data_sources.md",
                "output_requirements": "step-done/output_requirements.md"
            },
            # Special entry for update-input-components integration
            ("update-input-components", 1): {
                "framework_info": "update-input-components/framework_info.md",
                "step_info": "update-input-components/step_info.md",
                "data_sources": "update-input-components/data_sources.md",
                "output_requirements": "update-input-components/output_requirements.md"
            }
        }
    
    def _validate_paths(self):
        """Validate that required directory structure exists"""
        # Check if input_components directory exists
        if not self.components_dir.exists():
            raise FileNotFoundError(f"❌ Cannot find input_components directory at: {self.components_dir.absolute()}")
        
        # Create active directory if it doesn't exist
        if not self.active_dir.exists():
            try:
                self.active_dir.mkdir(parents=True, exist_ok=True)
                print(f"✅ Created active directory at: {self.active_dir.absolute()}")
            except Exception as e:
                raise FileNotFoundError(f"❌ Cannot create active directory at: {self.active_dir.absolute()}: {e}")
            
        # Check if meta directory exists, create if missing
        if not self.meta_dir.exists():
            try:
                self.meta_dir.mkdir(parents=True, exist_ok=True)
                print(f"✅ Created meta directory at: {self.meta_dir.absolute()}")
            except Exception as e:
                raise FileNotFoundError(f"❌ Cannot create meta directory at: {self.meta_dir.absolute()}: {e}")
        
        # Validate key input component files exist
        self._validate_input_components()
        
        print(f"✅ Path validation successful. Working from: {Path.cwd().absolute()}")
        print(f"✅ Framework state will be saved to: {self.state_file.absolute()}")
    
    def _validate_input_components(self):
        """Validate that required input component files exist"""
        # Check a few key input component files to ensure structure is correct
        key_files = [
            "step1/step_info.md",
            "step1/data_sources.md", 
            "step1/output_requirements.md",
            "step2/step_info.md"
        ]
        
        missing_files = []
        for file_path in key_files:
            full_path = self.components_dir / file_path
            if not full_path.exists():
                missing_files.append(str(full_path))
        
        if missing_files:
            raise FileNotFoundError(f"❌ Missing input component files: {', '.join(missing_files)}")
        
        print(f"✅ Input components validation successful. Found files in: {self.components_dir.absolute()}")
    
    def load_current_state(self):
        """Load current framework state"""
        if not self.state_file.exists():
            return None
        
        try:
            with open(self.state_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None
    
    def save_state(self, state_data):
        """Save framework state"""
        try:
            self.state_file.parent.mkdir(exist_ok=True)
            with open(self.state_file, 'w') as f:
                json.dump(state_data, f, indent=2)
        except PermissionError as e:
            raise Exception(f"❌ Permission denied writing to {self.state_file.absolute()}: {e}")
        except Exception as e:
            raise Exception(f"❌ Failed to save state to {self.state_file.absolute()}: {e}")
    
    def start_new_problem(self, problem_description):
        """Initialize new six-step session"""
        try:
            # Delete existing state file if it exists to ensure fresh start
            if self.state_file.exists():
                try:
                    self.state_file.unlink()
                    print(f"🗑️  Cleared existing state file: {self.state_file.absolute()}")
                except Exception as e:
                    print(f"⚠️  Warning: Could not clear existing state file: {e}")

            # Generate problem ID from description
            problem_id = problem_description.lower().replace(' ', '_').replace('-', '_')
            problem_id = ''.join(c for c in problem_id if c.isalnum() or c == '_')[:30]
            print(f"🆔 Generated problem ID: {problem_id}")
            
            # Create problem directory in active
            problem_dir = self.active_dir / problem_id
            try:
                problem_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created active directory: {problem_dir.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create active problem directory {problem_dir.absolute()}: {e}")
            
            # Create problem directory in meta for logging
            meta_problem_dir = self.meta_dir / problem_id
            try:
                meta_problem_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created meta directory: {meta_problem_dir.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create meta problem directory {meta_problem_dir.absolute()}: {e}")

            # Create user-review, guide, and input_dump subdirectories
            user_review_dir = problem_dir / "user-review"
            guide_dir = problem_dir / "guide"
            input_dump_dir = problem_dir / "input_dump"

            try:
                user_review_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created user-review directory: {user_review_dir.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create user-review directory {user_review_dir.absolute()}: {e}")

            try:
                guide_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created guide directory: {guide_dir.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create guide directory {guide_dir.absolute()}: {e}")

            try:
                input_dump_dir.mkdir(parents=True, exist_ok=True)
                print(f"📁 Created input_dump directory: {input_dump_dir.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create input_dump directory {input_dump_dir.absolute()}: {e}")
            
            # Initialize state
            state_data = {
                "problem_id": problem_id,
                "problem_description": problem_description,
                "current_step": "1",
                "current_phase": 1,
                "started": datetime.now().isoformat(),
                "status": "ACTIVE",
                "problem_dir": str(problem_dir)
            }
            
            # Save state with error handling
            try:
                self.save_state(state_data)
                print(f"💾 Saved state to: {self.state_file.absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to save state file: {e}")
            
            # Create STATE.md in problem directory
            state_md_content = f"""# Problem: {problem_description}
**Status**: ACTIVE
**Current Step**: 1 - Understanding Problem Statement
**Current Phase**: 1
**Started**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Progress Overview
- [ ] Step 1: Understanding Problem Statement
- [ ] Step 2: Current Situation Assessment
- [ ] Step 3: Brainstorming Session
- [ ] Step 4: Implementation
- [ ] Step 5: Testing & Optimization  
- [ ] Step 6: Insights Extraction

## Session Log
- {datetime.now().strftime('%H:%M')} User: Started six-step framework for: {problem_description}
"""
            
            try:
                with open(problem_dir / "STATE.md", 'w') as f:
                    f.write(state_md_content)
                print(f"📝 Created STATE.md: {(problem_dir / 'STATE.md').absolute()}")
            except Exception as e:
                raise Exception(f"❌ Failed to create STATE.md file: {e}")
            
            return state_data
            
        except Exception as e:
            print(f"❌ Error in start_new_problem: {e}")
            raise
    
    def advance_step_phase(self):
        """Move to next step or phase"""
        current_state = self.load_current_state()
        if not current_state:
            return "No active six-step session found"
        
        step = current_state["current_step"]
        phase = current_state["current_phase"]
        
        # Check if current step has more phases
        if phase < len(self.steps[step]["phases"]):
            # Advance to next phase
            current_state["current_phase"] = phase + 1
            new_step_name = f"{step} - {self.steps[step]['name']}"
            new_phase_info = f"Phase {phase + 1}"
        else:
            # Advance to next step
            next_step = str(int(step) + 1)
            if next_step in self.steps:
                current_state["current_step"] = next_step
                current_state["current_phase"] = 1
                new_step_name = f"{next_step} - {self.steps[next_step]['name']}"
                new_phase_info = "Phase 1"
            else:
                # Step 6 is complete - move to completed directory and reset state
                if step == "6":
                    return self._complete_framework_session(current_state)
                else:
                    return "Framework complete - all 6 steps finished"
        
        self.save_state(current_state)
        
        # Update STATE.md
        self._update_state_md(current_state, new_step_name, new_phase_info)
        
        return f"Advanced to Step {current_state['current_step']}, {new_phase_info}: {new_step_name}"
    
    def _update_state_md(self, state_data, step_name, phase_info):
        """Update STATE.md file"""
        problem_dir = Path(state_data["problem_dir"])
        state_md = problem_dir / "STATE.md"
        
        if state_md.exists():
            with open(state_md, 'r') as f:
                content = f.read()
            
            # Update current step line
            updated_content = ""
            for line in content.split('\n'):
                if line.startswith('**Current Step**:'):
                    updated_content += f"**Current Step**: {step_name}\n"
                elif line.startswith('**Current Phase**:'):
                    updated_content += f"**Current Phase**: {phase_info}\n"
                else:
                    updated_content += line + "\n"
            
            with open(state_md, 'w') as f:
                f.write(updated_content.rstrip() + "\n")
    
    def _complete_framework_session(self, current_state):
        """Complete framework session: move to completed directory and reset state"""
        import shutil
        
        problem_id = current_state["problem_id"]
        problem_dir = Path(current_state["problem_dir"])
        
        # Ensure completed directory exists
        self.completed_dir.mkdir(parents=True, exist_ok=True)
        
        # Move active directory to completed
        completed_problem_dir = self.completed_dir / problem_id
        try:
            if completed_problem_dir.exists():
                # If directory already exists, create a unique name with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                completed_problem_dir = self.completed_dir / f"{problem_id}_{timestamp}"
            
            shutil.move(str(problem_dir), str(completed_problem_dir))
            print(f"📁 Moved {problem_id} to completed: {completed_problem_dir}")
            
            # Update STATE.md in completed directory to mark as COMPLETE
            completed_state_md = completed_problem_dir / "STATE.md"
            if completed_state_md.exists():
                with open(completed_state_md, 'r') as f:
                    content = f.read()
                
                # Update status and completion info
                updated_content = ""
                for line in content.split('\n'):
                    if line.startswith('**Status**:'):
                        updated_content += "**Status**: COMPLETE ✅\n"
                    elif line.startswith('**Current Step**:'):
                        updated_content += "**Current Step**: 6 - Insights Extraction\n"
                    elif line.startswith('**Current Phase**:'):
                        updated_content += "**Current Phase**: Phase 1  \n"
                    elif '**Started**:' in line:
                        updated_content += line + "\n"
                        updated_content += f"**Completed**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                    else:
                        updated_content += line + "\n"
                
                with open(completed_state_md, 'w') as f:
                    f.write(updated_content.rstrip() + "\n")
            
        except Exception as e:
            return f"❌ Error moving to completed directory: {e}"
        
        # Clear current state
        try:
            if self.state_file.exists():
                self.state_file.unlink()
                print(f"🗑️  Cleared current state file")
        except Exception as e:
            print(f"⚠️  Warning: Could not clear state file: {e}")
        
        return f"✅ Framework session completed! Problem '{problem_id}' moved to completed directory and state reset."
    
    def get_input_components(self):
        """Get input components for current step/phase (detection-logic)"""
        current_state = self.load_current_state()
        if not current_state:
            return None
        
        step = current_state["current_step"]
        phase = current_state["current_phase"]
        
        key = (step, phase)
        if key in self.input_component_files:
            component_files = self.input_component_files[key]
            components = {}
            
            # Read common framework info first
            if self.framework_info_file.exists():
                with open(self.framework_info_file, 'r') as f:
                    components["framework_info"] = f.read().strip()
            else:
                components["framework_info"] = "❌ Missing framework_info.md"
            
            # Read step-specific components
            for component_type, filename in component_files.items():
                file_path = self.components_dir / filename
                if file_path.exists():
                    with open(file_path, 'r') as f:
                        components[component_type] = f.read().strip()
                else:
                    components[component_type] = f"❌ Missing file: {filename}"
            
            # Add problem context
            components["problem_id"] = current_state["problem_id"]
            components["problem_description"] = current_state["problem_description"]
            return components
        
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python framework_state.py [start|advance|status] [args...]")
        return
    
    state_manager = FrameworkState()
    command = sys.argv[1]
    
    if command == "start":
        if len(sys.argv) < 3:
            print("Usage: python framework_state.py start 'problem description'")
            return
        problem_desc = " ".join(sys.argv[2:])
        result = state_manager.start_new_problem(problem_desc)
        print(f"✅ Started six-step framework for: {problem_desc}")
        print(f"📁 Problem ID: {result['problem_id']}")
        print(f"📍 Current: Step 1, Phase 1")
        print()
        print("## Framework Initialization Complete")
        print()
        print("✅ Six-step framework has been initialized for your problem.")
        print("📁 Directory structure and STATE.md have been created.")
        print("🎯 Framework is now ready for use.")
        print()
        print("**Next Steps:**")
        print("Use the `/sixstep` command to begin Step 1 of the framework. Do NOT start analyzing or solving the problem yet - wait for the user to explicitly begin the six-step process.")
        
    elif command == "advance":
        result = state_manager.advance_step_phase()
        print(f"➡️  {result}")
        
    elif command == "status":
        current_state = state_manager.load_current_state()
        if current_state:
            components = state_manager.get_input_components()
            print(f"📋 Active Problem: {current_state['problem_description']}")
            print(f"📁 Problem ID: {current_state['problem_id']}")
            print(f"📍 Current: Step {current_state['current_step']}, Phase {current_state['current_phase']}")
            if components:
                print(f"🎯 Framework Info: {components['framework_info']}")
                print(f"📝 Step Info: {components['step_info']}")
        else:
            print("❌ No active six-step session found")

if __name__ == "__main__":
    main()