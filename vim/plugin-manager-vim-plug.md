# Vim Plugin Manager "[Vim-Plug](https://github.com/junegunn/vim-plug)"

## Installation & Usage

1. Download [plug.vim](https://github.com/junegunn/vim-plug/blob/master/plug.vim) in `~/.vim/autoload`
2. Add a vim-plug section to your `~/.vimrc`

#### Example

```vim
call plug#begin('~/.vim/plugged')

" A Tree Explorer plugin for vim
Plug 'scrooloose/nerdtree'

" Syntax checking
Plug 'scrooloose/syntastic'

" Git wrapper
Plug 'tpope/vim-fugitive'

" Status/tabline for vim
Plug 'bling/vim-airline'

" A Code-completion engine
Plug 'valloric/youcompleteme', { 'do': './install.py' }

call plug#end()
```

3. Install Plugins
`:w`-> `:source %` -> `PlugInstall`
