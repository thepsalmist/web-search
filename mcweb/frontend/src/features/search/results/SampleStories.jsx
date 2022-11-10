import * as React from 'react';
import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import dayjs from 'dayjs';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';

import { useGetSampleStoriesMutation } from '../../../app/services/searchApi';
import queryGenerator from '../util/queryGenerator';
import {
  PROVIDER_REDDIT_PUSHSHIFT, PROVIDER_NEWS_MEDIA_CLOUD, PROVIDER_NEWS_WAYBACK_MACHINE,
  PROVIDER_TWITTER_TWITTER, PROVIDER_YOUTUBE_YOUTUBE,
} from '../util/platforms';

const supportsDownload = (platform) => [PROVIDER_NEWS_MEDIA_CLOUD, PROVIDER_NEWS_WAYBACK_MACHINE,
  PROVIDER_REDDIT_PUSHSHIFT, PROVIDER_TWITTER_TWITTER].includes(platform);

export default function SampleStories() {
  const {
    queryList,
    negatedQueryList,
    platform,
    startDate,
    endDate,
    collections,
    sources,
    lastSearchTime,
    anyAll,
  } = useSelector((state) => state.query);

  const queryString = queryGenerator(queryList, negatedQueryList, platform, anyAll);

  const [query, { isLoading, data }] = useGetSampleStoriesMutation();

  const collectionIds = collections.map((collection) => collection.id);

  const handleDownloadRequest = (queryObject) => {
    window.location = `/api/search/download-all-content-csv?queryObject=${encodeURIComponent(JSON.stringify(queryObject))}`;
  };

  useEffect(() => {
    if (queryList[0].length !== 0) {
      query({
        query: queryString,
        startDate,
        endDate,
        collections: collectionIds,
        sources,
        platform,

      });
    }
  }, [lastSearchTime]);

  if (isLoading) {
    return (
      <div>
        {' '}
        <CircularProgress size="75px" />
        {' '}
      </div>
    );
  }
  if (!data) return null;

  const content = (
    <div className="results-item-wrapper results-sample-stories">
      <div className="row">
        <div className="col-4">
          <h2>Sample Content</h2>
          <p>
            This is a sample of the content that matched your queries.
            Click the menu on the bottom  right to download a CSV of all the
            matching content and associated metadata.
          </p>
          { (platform === PROVIDER_NEWS_MEDIA_CLOUD) && (
            <p>
              These results are a random sample of news stories that matched your searches.
            </p>
          )}
          { (platform === PROVIDER_REDDIT_PUSHSHIFT) && (
            <p>
              These results are the top scoring Reddit submissions that matched your
              searches.
            </p>
          )}
          { (platform === PROVIDER_TWITTER_TWITTER) && (
            <p>
              These results are the most recent tweets that matched your searches.
            </p>
          )}
          { (platform === PROVIDER_YOUTUBE_YOUTUBE) && (
            <p>
              These results are the most viewed videos that matched your searches.
            </p>
          )}
        </div>
        <div className="col-8">
          <table>
            <tbody>
              <tr>
                <th>Title</th>
                <th>Source</th>
                <th>Publication Date</th>
              </tr>
              {data.sample.map((sampleStory) => (
                <tr key={`story-${sampleStory.id}`}>
                  <td><a href={sampleStory.url} target="_blank" rel="noreferrer">{sampleStory.title}</a></td>
                  <td>
                    {(platform === PROVIDER_NEWS_MEDIA_CLOUD) && (
                    <img
                      className="google-icon"
                      src={`https://www.google.com/s2/favicons?domain=${sampleStory.media_url}`}
                      alt="{sampleStory.media_name}"
                    />
                    )}
                    <a href={sampleStory.media_url} target="_blank" rel="noreferrer">{sampleStory.media_name}</a>
                  </td>
                  <td>{dayjs(sampleStory.publish_date).format('MM-DD-YY')}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );

  let platformSpecficContent;
  if (supportsDownload(platform)) {
    platformSpecficContent = (
      <div className="clearfix">
        <div className="float-end">
          <Button
            variant="text"
            onClick={() => {
              handleDownloadRequest({
                query: queryString,
                startDate,
                endDate,
                collections: collectionIds,
                sources,
                platform,
              });
            }}
          >
            Download CSV
          </Button>
        </div>
      </div>
    );
  }
  return (
    <>
      {content}
      {platformSpecficContent}
    </>
  );
}
