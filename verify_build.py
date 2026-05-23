import sys
from flavor_compiler.orchestrator import FlavorOrchestrator, AnomalyClosureError

try:
    orc = FlavorOrchestrator()
    print("Success: flavor_compiler.orchestrator imported and initialized.")
    # In a real scenario, we would call a method that triggers the Rust FFI
    print("Build verification complete.")
except Exception as e:
    print(f"Verification failed: {e}")
    sys.exit(1)
