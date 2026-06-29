$root = "SRC\opg"

Get-ChildItem -Path $root -Recurse -File | ForEach-Object {

    if ($_.Name -match "^__init__.*Copie.*\.py$") {

        $target = Join-Path $_.Directory.FullName "__init__.py"

        if (-not (Test-Path $target)) {

            Write-Host "Rename :" $_.FullName
            Rename-Item $_.FullName "__init__.py"

        }
        else {

            Write-Host "Delete duplicate :" $_.FullName
            Remove-Item $_.FullName

        }
    }
}