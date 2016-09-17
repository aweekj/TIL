# How to set up [YouCompleteMe(YCM)](https://github.com/valloric/youcompleteme) for Vim

> Installation for Mac OS X

1. Install YCM using plugin manager like Vim-plug or Vundle

플러그인 매니저를 사용해서 YCM을 설치한다. 필자는 vim-plug를 사용하였으며 아래와 같이 추가하였다.

```vim
call plug#begin('~/.vim/plugged')
...
Plug 'valloric/youcompleteme'
...
call plug#end()
```

2. Install CMake if you want C-family completion

C 계열의 언어를 지원하려면 `CMake`를 설치해야 한다. 또한, `clang`을 사용하므로 `Command Line Tool`이 설치 되어 있어야 한다.(최신 버전의 Xcode를 설치하면 함께 설치 됨.)

```
$ brew updates
$ brew install cmake
```

NOTE: `CMake` 설치 중 아래와 같은 에러가 나서, 접근권한을 변경하여 해결하였다.

```
Error: Could not symlink share/man/man7/cmake-buildsystem.7
/usr/local/share/man/man7 is not writable.
```
```bash
$ sudo chmod 777 /usr/local/share/man/man7
$ brew link cmake
```

3. Compile YCM

```bash
$ cd ~/.vim/bundle/YouCompleteMe
$ ./install.py --clang-completer
```

4. Config

`.vimrc` 파일에 아래 내용을 추가한다.

```vim
" <YouCompleteMe> {{
let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
let g:ycm_confirm_extra_conf = 0
let g:ycm_key_list_select_completion = ['<C-j>', '<Down>']
let g:ycm_key_list_previous_completion = ['<C-k>', '<Up>']
let g:ycm_autoclose_preview_window_after_completion = 1
let g:ycm_min_num_of_chars_for_completion = 1
let g:ycm_auto_trigger = 0
let g:ycm_python_binary_path = '/usr/local/bin/python3'

nnoremap <leader>g :YcmCompleter GoTo<CR>
nnoremap <leader>gg :YcmCompleter GoToImprecise<CR>
nnoremap <leader>d :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>t :YcmCompleter GetType<CR>
nnoremap <leader>p :YcmCompleter GetParent<CR>
" }}
```

5. Usage

ctrl + space 을 입력하거나, (C의 경우) `.`이나 `->`을 입력하면 자동 완성 목록이 나타난다.


## 참고
- [https://github.com/valloric/youcompleteme](https://github.com/valloric/youcompleteme)
- [http://nophotoplease.tistory.com/6](http://nophotoplease.tistory.com/6)
- [http://neverapple88.tistory.com/26](http://neverapple88.tistory.com/26)
