import { Box, Typography } from "@mui/material";

const EmptyFilters = function (): JSX.Element {
  return (
    <Box className="flex flex-col w-full h-full align-middle items-center justify-center gap-2">
      <Typography className="text-gray-500" variant="body2" fontSize="medium">
        No results matching the current filters.
      </Typography>
      <Typography className="text-gray-500" variant="body2" fontSize="medium">
        Clear the filters to see all results.
      </Typography>
    </Box>
  );
};

export default EmptyFilters;
