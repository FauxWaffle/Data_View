$pip_find = pip list | Out-String

if ($pip_find -notmatch 'streamlit' -or 'pandas') {
    pip install streamlit --user
    pip install pandas --user
}

$data_array = @()

$index = Read-Host "Enter UNC Path(s) separated paths by commas"
$paths = $index -split ','
$is_recurse = Read-Host "If recursive, type: -recurse, if not, press Enter"

foreach ($path in $paths) {
    # Iterate over $paths, not $index
    $path = $path.Trim()
    if ($path.Contains(' ')) {
        $path = "`"$path`""
    }
    
    if ($is_recurse -eq "-recurse") {
        $data_array += @(Get-ChildItem -Path $path -File -Recurse)
    }
    else {
        write-host($path)
        $data_array += @(Get-ChildItem -Path $path -File)
        
    }
}

$noTouch = @()
$results = @()

foreach ($file in $data_array) {
    $file_owner = $file | Get-Acl | select -ExpandProperty Owner

    $results += New-Object PSObject -Property ([ordered]@{
            'File Name'   = $file.Name
            'File Size'   = $file.Length / 1000
            'File Owner'  = $file_owner
            'Created On'  = $file.CreationTime
            'Last Access' = $file.LastAccessTime
            'Last Touch'  = $file.LastWriteTime
        })

    foreach ($filename in $data_array) {
        if ($file.CreationTime -eq $file.LastAccessTime) {
            $noTouch += $filename
        }
        
    }

    
}
$noTouch | Export-Csv -Path .\CSV\notouch.csv -NoTypeInformation
$results | Export-Csv -Path .\CSV\datafile.csv -NoTypeInformation

streamlit run main_st.py
