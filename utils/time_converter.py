from datetime import datetime


def time_since(timestamp: int) -> str:
    """
    Convert timestamp to human readable

    Args:
        timestamp: unix timestamp

    Returns: seconds, min, hour, day

    Examples: 36 seconds ago
    """
    now = datetime.now()
    diff = now - datetime.fromtimestamp(timestamp / 1000.0)  # convert ms -> s

    if diff.total_seconds() < 60:
        return f"{diff.total_seconds()} seconds ago"
    elif diff.total_seconds() < 3600:
        minutes = int(diff.total_seconds() // 60)
        seconds = int(diff.total_seconds() % 60)
        return f"{minutes} minute{(minutes != 1 and 's')} and {seconds} second{'s' if seconds > 1 else ''} ago"
    elif diff.total_seconds() < 86400:
        hours = int(diff.total_seconds() // 3600)
        minutes = int((diff.total_seconds() % 3600) // 60)
        return f"{hours} hour{'s' if hours > 1 else ''} and {minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        days = int(diff.total_seconds() // 86400)
        hours = int(((diff.total_seconds() % 86400) // 3600))
        return f"{days} day{'s' if days > 1 else ''} and {hours} hour{'s' if hours > 1 else ''} ago"
