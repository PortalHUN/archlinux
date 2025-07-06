#
# ~/.bashrc
#

eval "$(starship init bash)"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls -l --color=auto'
alias grep='grep --color=auto'
alias nano='nvim'
alias vim='nvim'
alias cat='bat'
alias update-local-desktop-database='update-desktop-database ~/.local/share/applications'

PS1='[\u@\h \W]\$ '

export PATH=~/.local/bin:$PATH
