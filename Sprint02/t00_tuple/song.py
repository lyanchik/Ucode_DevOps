def song(verses,chorus): 
    final_song = ()
    for i in verses:
        final_song += i + chorus
    final_song += chorus
    return final_song
