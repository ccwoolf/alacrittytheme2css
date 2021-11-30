# alacrittytheme2css

This is a simple script to convert Alacritty themes/colour schemes to CSS variables. This makes it easy to use nice colour schemes in CSS without much manual work. It also makes it easy to swap files out to see what alternative themes look like.

## Usage

```shell
alacrittytheme2css.py path/to/theme.yaml
```

This will convert the Alacritty YAML to CSS and write it to `theme.css` in `$PWD` (where you ran the script from).

## Finding themes

The Alacritty wiki has many themes: https://github.com/alacritty/alacritty/wiki/Color-schemes.

Collections of individual colour schemes can be found elsewhere on Github, for example at https://github.com/eendroroy/alacritty-theme and https://github.com/dchakro/alacritty_colors.

## Theme YAML structure

The theme YAML structure should be the same that you would find in your `alacritty.yml` file. For example:

```yaml
colors:
  primary:
    background: '#1d1f21'
    foreground: '#c5c8c6'

  normal:
    black: '#1d1f21'
    red: '#cc6666'
    green: '#b5bd68'
    yellow: '#f0c674'
    blue: '#81a2be'
    magenta: '#b294bb'
    cyan: '#8abeb7'
    white: '#c5c8c6'

  bright:
    black: '#666666'
    red: '#d54e53'
    green: '#b9ca4a'
    yellow: '#e7c547'
    blue: '#7aa6da'
    magenta: '#c397d8'
    cyan: '#70c0b1'
    white: '#eaeaea'

  dim:
    black: '#131415'
    red: '#864343'
    green: '#777c44'
    yellow: '#9e824c'
    blue: '#556a7d'
    magenta: '#75617b'
    cyan: '#5b7d78'
    white: '#828482'
  ```

## Output CSS

`normal` colours won't have a prefix, but others, such as `bright` and `dim` will.

Running the script against the above YAML will produce the following CSS:

```css
:root {
  --background: #1d1f21;
  --foreground: #c5c8c6;
  --black: #1d1f21;
  --red: #cc6666;
  --green: #b5bd68;
  --yellow: #f0c674;
  --blue: #81a2be;
  --magenta: #b294bb;
  --cyan: #8abeb7;
  --white: #c5c8c6;
  --bright-black: #666666;
  --bright-red: #d54e53;
  --bright-green: #b9ca4a;
  --bright-yellow: #e7c547;
  --bright-blue: #7aa6da;
  --bright-magenta: #c397d8;
  --bright-cyan: #70c0b1;
  --bright-white: #eaeaea;
  --dim-black: #131415;
  --dim-red: #864343;
  --dim-green: #777c44;
  --dim-yellow: #9e824c;
  --dim-blue: #556a7d;
  --dim-magenta: #75617b;
  --dim-cyan: #5b7d78;
  --dim-white: #828482;
}
```
