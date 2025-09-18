#!/bin/bash

target_dir=$(
    fd -t d -d 1 |
        sed 's:/$::' |
        fzf --preview '
            echo -e "{}\n\n---" &&
                DIR=$(pwd) &&
                [ -d "$DIR"/{} ] &&
                tree -C "$DIR"/{} |
                head -200
            '
)
[[ -z "$target_dir" ]] && exit 0

dockerfile_name="Dockerfile"
compose_file_name="compose.yml"

if [ -z "$(ls -la ./$target_dir | grep $compose_file_name)" ]; then
    target_dockerfile="./$target_dir/$dockerfile_name"
    app_name="$target_dir-image"
    docker build -f "$target_dockerfile" -t "$app_name" "./$target_dir"
    docker run --rm "$app_name"
else
    target_compose="./$target_dir/$compose_file_name"
    docker compose -f "$target_compose" build
    docker compose -f "$target_compose" up --force-recreate
fi
