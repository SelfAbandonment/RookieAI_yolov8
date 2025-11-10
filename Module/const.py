"""
Constants for RookieAI configuration
Centralized constants for better maintainability and performance tuning
"""

# Trigger method mapping
method_mode = {
    "按下": "press",
    "切换": "toggle",
    "shift+按下": "shift+press"
}

# Performance constants
FRAME_CAPTURE_WIDTH = 320
FRAME_CAPTURE_HEIGHT = 320
DEFAULT_TARGET_FPS = 20
DEFAULT_FRAME_INTERVAL = 1.0 / DEFAULT_TARGET_FPS  # 0.05 seconds

# UI constants
DEFAULT_WINDOW_WIDTH = 1290
DEFAULT_WINDOW_HEIGHT = 585
DEFAULT_ANIMATION_DURATION = 500  # milliseconds
FPS_UPDATE_INTERVAL = 1.0  # seconds

# Model warmup constants
MODEL_WARMUP_CONF = 0.01  # Low confidence for faster warmup

# Shared memory constants
MAX_RETRIES = 3
RETRY_DELAY_BASE = 0.1  # seconds

# Performance monitoring
FRAME_TIME_SAMPLES = 100  # Number of frame times to keep for averaging
