def get_lyrics(melody):
    return melody.replace("C#", "c")\
                 .replace("D#", "d")\
                 .replace("F#", "f")\
                 .replace("G#", "g")\
                 .replace("A#", "a")\


def get_time(start, end):
    hour = int(start[:2]) - int(end[:2])
    minute = int(start[3:5]) - int(end[3:5])
    time = (60 * hour) + minute

    return time


def solution(m, musicinfos):
    ans = '(None)'
    max_melody = 0

    m = get_lyrics(m)

    for music in musicinfos:
        music = music.split(',')
        time = get_time(music[1], music[0])
        lyrics = get_lyrics(music[3])

        lyrics *= (time // len(lyrics)) + 1
        melody = lyrics[:time]

        if m in melody and time > max_melody:
            max_melody = time
            ans = music[2]

    return ans