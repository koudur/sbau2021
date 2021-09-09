from webassets.filter.postcss import PostCSS


class RootPostCSS(PostCSS):
    """Variation of PostCSS filter that does not change working
    directory."""

    name = 'root_postcss'

    def input(self, in_, out, source_path, **kw):
        args = [self.binary or 'postcss']
        if self.extra_args:
            args.extend(self.extra_args)

        self.subprocess(args, out, in_)
