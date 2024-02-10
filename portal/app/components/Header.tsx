import { AppBar, Box, Toolbar, Typography } from "@mui/material";
import Link from "next/link";

const Header = function (): JSX.Element {
  return (
    <AppBar position="fixed" className="h-14 flex justify-center bg-slate-700">
      <Toolbar className="flex h-full flex-row justify-between">
        <Box className="flex flex-row gap-2 items-center">
          <Link href="/">
            <Typography
              className="text-white font-mono font-extralight"
              textTransform="uppercase"
            >
              Irish Properties Prices
            </Typography>
          </Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
