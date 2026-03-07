# convert seconds to hours, minutes and seconds
def seconds_to_hms(inpute_seconds: int) -> tuple[int, int, int]:
    hour: int = inpute_seconds // 3600
    minute: int = (inpute_seconds % 3600) // 60
    seconds: int = ((inpute_seconds % 3600) % 60) 

    return (hour, minute, seconds)