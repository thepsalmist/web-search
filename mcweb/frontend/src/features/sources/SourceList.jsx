import * as React from 'react';
import PropTypes from 'prop-types';
import CircularProgress from '@mui/material/CircularProgress';
import { Link } from 'react-router-dom';
import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import IconButton from '@mui/material/IconButton';

import { useGetCollectionAssociationsQuery, useDeleteSourceCollectionAssociationMutation } from '../../app/services/sourcesCollectionsApi';

export default function SourceList(props) {
  const { collectionId, edit } = props;
  const {
    data,
    isLoading,
  } = useGetCollectionAssociationsQuery(collectionId);

  const [deleteSourceCollectionAssociation] = useDeleteSourceCollectionAssociationMutation();

  // if loading
  if (isLoading) {
    return (
      <div>
        {' '}
        <CircularProgress size="75px" />
        {' '}
      </div>
    );
  }

  return (
    <div>
      <h2>
        Sources (
        {data.sources.length}
        )
      </h2>
      <table width="100%">
        <thead>
          <tr>
            <th colSpan={edit ? 3 : 2}>Name</th>
          </tr>
        </thead>
        <tbody>
          {data.sources.map((source) => (
            <tr key={source.id}>
              <td>
                <a href={source.homepage} target="_new">
                  <img
                    className="google-icon"
                    src={`https://www.google.com/s2/favicons?domain=${source.name}`}
                    alt="{source.name}"
                  />
                </a>
              </td>
              <td>
                <Link to={`/sources/${source.id}`}>
                  {source.label || source.name}
                </Link>
              </td>
              {edit && (
                <td>
                  <IconButton
                    aria-label="remove"
                    onClick={() => {
                      deleteSourceCollectionAssociation({
                        source_id: source.id,
                        collection_id: collectionId,
                      });
                    }}
                  >
                    <HighlightOffIcon />
                  </IconButton>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

SourceList.propTypes = {
  collectionId: PropTypes.number.isRequired,
  edit: PropTypes.bool,
};

SourceList.defaultProps = {
  edit: false,
};
