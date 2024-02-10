import {
  Box,
  Grid,
  Stack,
  ToggleButton,
  ToggleButtonGroup,
  Typography,
} from "@mui/material";
import { InfiniteHits, useInstantSearch, useStats } from "react-instantsearch";
import SearchHit from "./SearchHit";
import SearchBar from "./SearchBar";
import EmptyHits from "./EmptyHits";
import SearchCurrentRefinements from "./CurrentRefinements";
import SearchGraph from "./SearchGraph";
import ListIcon from "@mui/icons-material/List";
import BarChartIcon from "@mui/icons-material/BarChart";
import { useState } from "react";
import { SearchView } from "../types/models";

const Search = function (): JSX.Element {
  const { results } = useInstantSearch();
  const { nbHits } = useStats();
  const [view, setView] = useState<SearchView>(SearchView.LIST);

  return (
    <Stack className="h-full w-full gap-5 pt-5">
      <SearchBar />
      <Grid container className="flex w-full h-full overflow-y-auto">
        <Grid item sm={0} md={0} lg={2} />
        <Grid
          item
          sm={12}
          md={12}
          lg={8}
          className="flex flex-col w-full h-full align-middle items-center"
        >
          <>
            {!results.__isArtificial && results.nbHits === 0 ? (
              <EmptyHits />
            ) : (
              <>
                <Box className="flex w-full flex-row-reverse">
                  <ToggleButtonGroup
                    color="primary"
                    exclusive
                    value={view}
                    defaultValue={SearchView.LIST}
                    size="small"
                    onChange={(_event, value) => setView(value)}
                  >
                    <ToggleButton value={SearchView.LIST}>
                      <ListIcon />
                    </ToggleButton>
                    <ToggleButton value={SearchView.GRAPH}>
                      <BarChartIcon />
                    </ToggleButton>
                  </ToggleButtonGroup>
                </Box>
                <SearchCurrentRefinements />
                {view == SearchView.GRAPH && <SearchGraph />}
                {view == SearchView.LIST && (
                  <>
                    <Typography
                      className="text-gray-400"
                      variant="caption"
                      fontSize="small"
                    >
                      {nbHits} results found
                    </Typography>
                    <InfiniteHits
                      classNames={{
                        root: "SearchInfiniteHits",
                        list: "SearchInfiniteHitsList",
                        item: "SearchInfiniteHitsItem",
                        loadMore: "SearchInfiniteLoadMore",
                      }}
                      hitComponent={SearchHit}
                      showPrevious={false}
                    />
                  </>
                )}
              </>
            )}
          </>
        </Grid>
        <Grid item sm={0} md={0} lg={2} />
      </Grid>
    </Stack>
  );
};

export default Search;
