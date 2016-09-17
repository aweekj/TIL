# Vim Plugin Manager - Vundle

## Installation

If you use Mac OS, Vim is already installed.

## Set Plugins

### Use [Vundle](https://github.com/VundleVim/Vundle.Vim)

```bash
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
$ vim ~/.vimrc
```

```vim
set nocompatible              " be iMproved, required
filetype off                  " required

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on

" Put your non-Plugin stuff after this line
```

`:w` -> `:source %` -> `:PluginInstall`

or

`:wq` -> `$ vim +PluginInstall +qall`

## My Plugin List

[http://vimawesome.com](http://vimawesome.com)

```vim
Plugin 'tpope/vim-sensible'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/nerdcommenter'
Plugin 'scrooloose/syntastic'
Plugin 'mattn/emmet-vim'
Plugin 'valloric/youcompleteme'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'bling/vim-airline'
```

## To Study Vim

[http://www.openvim.com](http://www.openvim.com)
