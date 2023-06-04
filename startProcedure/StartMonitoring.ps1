### SET FOLDER TO WATCH + FILES TO WATCH + SUBFOLDERS YES/NO
    $watcher = New-Object System.IO.FileSystemWatcher
    $watcher.Path = "C:\notebookExtractsLink"
    $watcher.Filter = "*.txt"
    $watcher.IncludeSubdirectories = $true
    $watcher.EnableRaisingEvents = $true  

### DEFINE ACTIONS AFTER AN EVENT IS DETECTED
    $action = { $path = $Event.SourceEventArgs.FullPath
                $changeType = $Event.SourceEventArgs.ChangeType
                $logline = "$(Get-Date), $changeType, $path"
                Add-content "C:\Users\tbbgr\iCloudDrive\Home Projects\smartNotebook\log.txt" -value $logline
              }   
    
    $actionPython = { $path = $Event.SourceEventArgs.FullPath
                $changeType = $Event.SourceEventArgs.ChangeType
                $logline = "$(Get-Date), $changeType, $path"
                Add-content "C:\Users\tbbgr\iCloudDrive\Home Projects\smartNotebook\log.txt" -value $logline
                python -u "C:\Users\tbbgr\iCloudDrive\Home Projects\smartNotebook\startProcedure\summaryCompiler.py"
            }

### DECIDE WHICH EVENTS SHOULD BE WATCHED s
    Register-ObjectEvent $watcher "Created" -Action $action
    Register-ObjectEvent $watcher "Changed" -Action $action
    Register-ObjectEvent $watcher "Deleted" -Action $action
    Register-ObjectEvent $watcher "Renamed" -Action $actionPython
    while ($true) {sleep 5}