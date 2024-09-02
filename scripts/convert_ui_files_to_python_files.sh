#!/bin/bash

# Setze das Verzeichnis des Skripts als Arbeitsverzeichnis
SCRIPT_DIR="$(dirname "$0")"

# Setze die Verzeichnisse relativ zum Skriptverzeichnis
SOURCE_DIR="$SCRIPT_DIR/../src/gui/ui/static"
TARGET_DIR="$SCRIPT_DIR/../src/gui/ui"


# Schleife über alle .ui Dateien im Quellverzeichnis
for ui_file in "$SOURCE_DIR"/*.ui; do
    # Überprüfe, ob die Datei tatsächlich existiert
    if [ ! -f "$ui_file" ]; then
        echo "Keine .ui-Dateien gefunden im Verzeichnis $SOURCE_DIR"
        exit 1
    fi

    # Extrahiere den Dateinamen ohne Verzeichnis und Endung
    base_name=$(basename "$ui_file" .ui)
    # Füge das "ui_" Präfix zum Dateinamen hinzu
    target_name="ui_${base_name}.py"

    # Konvertiere die .ui Datei in eine .py Datei und speichere sie im Zielverzeichnis
    echo "Konvertiere $ui_file nach $TARGET_DIR/$target_name"
    pyside6-uic -g python "$ui_file" > "$TARGET_DIR/$target_name"

    if [ $? -ne 0 ]; then
        echo "Fehler bei der Konvertierung von $ui_file"
        exit 1
    fi
done

echo "Alle .ui Dateien wurden konvertiert."