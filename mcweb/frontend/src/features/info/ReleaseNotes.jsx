import React from 'react';

const sampleRelease = [
  {
    version: 'v1.2.9',
    date: '2023-01-17',
    notes: ['add top language and top words experimental features',
      'fixes to uploading sources',
      'fixes to multi-platform search',
      'limit searchable dates for WB online news'],
  },
  {
    version: 'v1.2.8',
    date: '2023-01-05',
    notes: ['add catch page for bad urls',
      'add capabilites to fetch stories from rss feed or source',
      'minor ui and ux updates',
      'add default dates to search date picker',
      'search bug fixes',
      'fix for support of downloading larger samples from twitter',
      'add multi-platform collections',
      'add source search to media picker'],
  },
  {
    version: 'v1.2.7',
    date: '2023-01-04',
    notes: ['add type to featured collections',
      'add rss syncing capabilities',
      'remove media cloud provider'],
  },
  {
    version: 'v1.2.6',
    date: '2022-12-23',
    notes: ['add feed detail page',
      'search bug fixes',
      'ui improvements',
      'rss api improvements',
      'add delete for sources and collections'],
  },
  {
    version: 'v1.2.5',
    date: '2022-12-19',
    notes: ['search bug fixes',
      'add support for public collections',
      'add share search button'],
  },
  {
    version: 'v1.2.2 - v1.2.4',
    date: '2022-12-12',
    notes: ['add multi-platform search functionality',
      'add rss feed management',
      'add system warning'],
  },
  {
    version: 'v1.2.1',
    date: '2022-12-09',
    notes: ['fix collection and source editing'],
  },
  {
    version: 'v1.2.0',
    date: '2022-12-08',
    notes: ['add pagination to list of sources',
      'add media weekly story counts'],
  },
  {
    version: 'v1.1.0',
    date: '2022-12-07',
    notes: ['major improvements to media picker',
      'search date fix',
      'language detection added',
      'add geographic collections',
      'major rss feed integration updates',
      'email cleanup'],
  },
  {
    version: 'v1.0.0',
    date: '2022-12-01',
    notes: ['add advanced search',
      'search bug fixes',
      'allow streaming download of sources',
      'add user quotas',
      'add email support',
      'allow downloading of search result charts',
      'add further user profile support',
      'add initial support of rss feeds for directory'],
  },
  {
    version: 'v0.1.4',
    date: '2022-11-10',
    notes: ['directory styling changes',
      'bug fixes in search results and downloading csvs'],
  },
  {
    version: 'v0.1.3',
    date: '2022-11-08',
    notes: ['add normalized url after searching', 'search bug fixes'],
  },
  {
    version: 'v0.1.2',
    date: '2022-11-03',
    notes: ['add directory feature',
      'add initial stying',
      'add featured online news collections',
      'add sources and collections',
      'add download sources csv',
      'add search capabilities',
      'major styling changes',
      'fixes to user auth'],
  },
  {
    version: 'v0.1.1',
    date: '2022-08-22',
    notes: ['add search api support', 'add docs and setup instructions'],
  },
  {
    version: 'v0.1.0',
    date: '2022-08-17',
    notes: ['app creation'],
  },
];
export default function ReleaseNotes() {
  return (
    <div className="container">
      {sampleRelease.map((release) => (
        <div key={release.version}>
          <h2>{release.version}</h2>
          <h5>
            Release Date:
            {' '}
            {release.date}
          </h5>
          <h5>Changes</h5>
          <ul>
            {release.notes.map((note) => (
              <li key={note}>
                {note}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
