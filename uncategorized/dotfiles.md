# Dotfiles

dotfiles 폴더에 `.bash_profile` `.vimrc` `.zshrc` 등 .(dot)으로 시작하는 설정 파일을 모아둔다. 이 때, 파일명의 .을 삭제하여 숨김을 해제한다. 그리고 원래 있던 위치에 심볼릭 링크를 만든다.

```bash
$ mkdir ~/dotfiles
$ mv ~/.vimrc ~/dotfiles/vimrc
$ ln -s ~/dotfiles/vimrc ~/.vimrc
```

### 참고
[http://dotfiles.github.io](http://dotfiles.github.io)에서 `dotfiles` 에 대한 정보와 다른 사람들의 `dotfiles` 를 볼 수 있다.
