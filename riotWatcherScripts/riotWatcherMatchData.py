import riotwatcher

watcher = riotwatcher.RiotWatcher("LOLOL")

print(watcher.champion.rotations("TRLH4"))

watcher.summoner.by_name("TRLH4", "Cobular")
