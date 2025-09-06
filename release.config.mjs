const PYPI_REPOSITORY = 'https://upload.pypi.org/legacy/';

export default {
    branches: ["main"],
    plugins: [
        ['@semantic-release/commit-analyzer', { preset: 'conventionalcommits' }],
        ['@semantic-release/release-notes-generator', { preset: 'conventionalcommits' }],
        ['@semantic-release/changelog', { changelogFile: 'docs/CHANGELOG.md' }],
        [
            '@semantic-release/exec',
            {
                prepareCmd: 'uv version ${nextRelease.version}',
                publishCmd: `uv build && uv publish --publish-url ${PYPI_REPOSITORY} --trusted-publishing always`,
            },
        ],
        [
            '@semantic-release/github',
            {
                assets: [
                    { path: 'dist/*.tar.gz', label: 'sdist' },
                    { path: 'dist/*.whl', label: 'wheel' },
                ],
            },
        ],
    ]
};
