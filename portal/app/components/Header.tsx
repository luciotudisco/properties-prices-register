import { Box, Typography } from "@mui/material";

const Header = function (): JSX.Element {
  return (
    <Box className="flex w-full h-full align-middle items-center bg-gray-100 border-t-2 border-gray-400 p-5">
      <Typography
        className="text-gray-900"
        variant="h1"
        fontSize="large"
        fontFamily="monospace"
      >
        Properties Prices Register
      </Typography>
    </Box>
  );
};

export default Header;
