{
  "targets": [
    {
      "target_name": "node-term-size",
      "sources": [
        "node-term-size.cc",
        "linux.cc",
        "win.cpp"
      ],
      'conditions': [
        ['OS != "linux"', {
          'sources!': [
            'linux.cc',
          ]
        }],
        ['OS != "win"', {
          'sources!': [
            'win.cpp',
          ]
        }]
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"]
    }
  ]
}
